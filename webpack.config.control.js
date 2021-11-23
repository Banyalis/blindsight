const path = require('path');
const fs = require('fs');
const webpack = require('webpack');
const autoprefixer = require('autoprefixer');
const BundleTracker = require('webpack-bundle-tracker');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const SVGSpritemapPlugin = require('svg-spritemap-webpack-plugin');
const WebpackShellPlugin = require('webpack-shell-plugin');
const {VueLoaderPlugin} = require('vue-loader');
const postcssPresetEnv = require('postcss-preset-env');
const CompressionPlugin = require('compression-webpack-plugin');

const NODE_ENV = process.env.NODE_ENV;
const isDevelopment = NODE_ENV === 'development';

const getPath = (folderName) => path.join(__dirname, folderName);

var jsonConfig = {};
try {
    jsonConfig = require('./config.json');
}
catch (e) {
    jsonConfig = require('./config.test.json');
}

// write static url const for LESS
fs.writeFileSync(path.join(__dirname, 'assets', 'app', 'control', 'styles', 'static-url.less'), '@static_url: \'' + (jsonConfig.HOT_RELOADING ? jsonConfig.STATIC_URL_HOT : jsonConfig.STATIC_URL) + '\';\n');


module.exports = {

    devtool: isDevelopment ? 'cheap-module-source-map' : 'sourcemap',

    mode: isDevelopment ? 'development' : 'production',

    entry: {
        control: getPath('./assets/app/control/App'),
        // login: getPath('./assets/app/control/Login')
    },

    output: {
        filename: isDevelopment ? 'app/[name]/main.js' : 'app/[name]/main.[hash].js',
        path: getPath('static'),
        publicPath: jsonConfig.HOT_RELOADING ? 'http://127.0.0.1:9999/static/' : undefined
    },

    resolve: {
        modules: [
            'node_modules',
            'assets/app',
            'assets/app/control/',
            'assets/custom_libs/',
            'assets/js/'
        ],
        alias: {
            'mixins': getPath('assets/app/control/utils/mixins')
        }
    },

    optimization: {},

    resolveLoader: {
        modules: [getPath('node_modules')]
    },

    devServer: {
        historyApiFallback: true,
        noInfo: false,
        headers: {
            "Access-Control-Allow-Origin": "\*",
        },
        contentBase: false,
        clientLogLevel: 'warning',
        port: 9999,
        hot: true
    },

    module: {
        rules: [
            // Используем eslint-loader как прелоадер, чтобы проверять js-исходники,
            // не измененные другими лоадерами как, например, babel-loader-ом.
            /*{
                test: /\.js$/,
                exclude: [
                    path.resolve(__dirname, 'node_modules'),
                    path.resolve(__dirname, 'assets/custom_libs'),
                    path.resolve(__dirname, 'assets/js')
                ],
                enforce: 'pre',
                use: [
                    {
                        loader: 'eslint-loader',
                        options: { cache: true }
                    }
                ]
            },*/
            {
                test: /reverse\.js$/,
                use: ['imports-loader?me=>{}', 'exports-loader?me.Urls']
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                        js: 'babel-loader'
                    }
                }
            },
            {
                test: /\.jinja$/,
                use: {
                    loader: 'nunjucks-loader',
                    options: {
                        config: __dirname + '/nunjucks.config.js'
                    }
                }
            },
            {
                test: /\.less$/,
                use: [
                    {
                        loader: jsonConfig.HOT_RELOADING ? "style-loader" : MiniCssExtractPlugin.loader
                    }, {
                        loader: "css-loader",
                    }, {
                        loader: 'postcss-loader',
                        options: {
                            plugins() {
                                return [
                                    postcssPresetEnv()
                                ];
                            }
                        }
                    }, {
                        loader: "less-loader"
                    }
                ]
            },
            {
                test: /\.css$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader
                    }, {
                        loader: "css-loader"
                    }, {
                        loader: 'postcss-loader',
                        options: {
                            plugins() {
                                return [
                                    postcssPresetEnv()
                                ];
                            }
                        }
                    }
                ]
            },
        ]
    },

    plugins: [
        new CleanWebpackPlugin([
            getPath('static/app/control'),
            getPath('static/app/login'),
            getPath('static/svg/control.sprite.svg')
        ], {root: getPath('')}),
        /*new WebpackShellPlugin({
            onBuildStart:['python manage.py collectstatic_js_reverse --settings=config.control_reverse']
        }),*/
        new MiniCssExtractPlugin({
            filename: isDevelopment ? 'app/[name]/main.css' : 'app/[name]/main.[hash].css'
        }),
        new webpack.DefinePlugin({
            'process.env': {
                isStaging: (NODE_ENV === 'development' || NODE_ENV === 'staging'),
                NODE_ENV: `"${NODE_ENV}"`
            }
        }),
        new webpack.ProvidePlugin({
            'mixins': 'mixins'
        }),
        new VueLoaderPlugin(),
        new SVGSpritemapPlugin(getPath('assets/svg/control/*.svg'), {
            output: {
                filename: 'svg/control.sprite.svg',
                svg4everybody: false,
                svgo: true
            },
            sprite: {
                prefix: false,
                generate: {
                    use: true
                }
            }
        }),
        new CompressionPlugin(),
        new BundleTracker({filename: './webpack.control.stats.json'})
    ],

    externals: {
        jquery: 'jQuery'
    },

    performance: {
        hints: false
    },

    stats: {
        colors: true,
        hash: false,
        version: false,
        timings: false,
        assets: false,
        chunks: false,
        modules: false,
        reasons: false,
        children: false,
        source: false,
        // errors: false,
        errorDetails: false,
        warnings: true,
        publicPath: false
    }
};
