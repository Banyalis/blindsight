import Vue from 'vue'
import VueRouter from 'vue-router'

// import {Page as Dummy} from './modules/dummy';
// import {Page as Dashboard} from './modules/dashboard';
// import {
//     OverviewPage as TrueOverview,
//     JoinPage as TrueJoin,
//     JoinPositionPage as TrueJoinPosition,
//     StoryPage as TrueStory,
//     TeamPage as TrueTeam,
//     TeamOverviewPage as TrueTeamOverview,
//     TeamPeoplePage as TrueTeamPeople,
//     NewsPage as TrueNewsPage,
//     NewsItemPage as TrueNewsItem,
//     ContactPage as TrueContact,
//     ContactChannelPage as TrueContactTrue,
// } from './modules/true';

// import {
//     OverviewPage as SearchOverview,
//     ExpertisePage as SearchExpertise,
//     ExpertiseCategoryPage as SearchExpertiseCategory,
//     RecentPlacementsPage as SearchRecentPlacements,
//     SearchPositionsPage as SearchPositions,
//     SearchPositionsItemPage as SeachPositionsItem,
// } from './modules/search';

// import {
//     OverviewPage as TechnologiesOverview,
// } from './modules/technologies';

// import {
//     OverviewPage as DevelopmentOverview,
// } from './modules/development';

// import {
//     ClientsPage as Clients,
//     Footer,
//     PrivacyPage as Privacy,
//     CMSAccessPage as CMSAccess,
//     Salesforce,
// } from './modules/utilities';

import store from './store';

import Urls from 'django_js_control/reverse.js';

Vue.use(VueRouter);

window.app_store = store;

const routes = [
    // {
    //     path: Urls['control:main'](),
    //     name: 'dashboard',
    //     component: Dashboard,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:true'](),
    //     name: 'true',
    //     component: Dummy,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:true-overview'](),
    //     name: 'true-overview',
    //     component: TrueOverview,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:true-join'](),
    //     name: 'true-join',
    //     component: TrueJoin,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:true-join-position'](':id'),
    //     name: 'true-join-position',
    //     component: TrueJoinPosition,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:true-story'](),
    //     name: 'true-story',
    //     component: TrueStory,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:true-team'](),
    //     name: 'true-team',
    //     component: TrueTeam,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:true-team-overview'](),
    //     name: 'true-team-overview',
    //     component: TrueTeamOverview,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:true-team-people'](),
    //     name: 'true-team-people',
    //     component: TrueTeamPeople,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:true-news'](),
    //     name: 'true-news',
    //     component: TrueNewsPage,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:true-news-item'](':id'),
    //     name: 'true-news-item',
    //     component: TrueNewsItem,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:true-contact'](),
    //     name: 'true-contact',
    //     component: TrueContact,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:true-contact-true'](),
    //     name: 'true-contact-true',
    //     component: TrueContactTrue,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:clients'](),
    //     name: 'clients',
    //     component: Clients,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:footer'](),
    //     name: 'footer',
    //     component: Footer,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:privacy'](),
    //     name: 'privacy',
    //     component: Privacy,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:access'](),
    //     name: 'access',
    //     component: CMSAccess,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:salesforce'](),
    //     name: 'salesforce',
    //     component: Salesforce,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:search-overview'](),
    //     name: 'search-overview',
    //     component: SearchOverview,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:search-industry'](),
    //     name: 'search-industry',
    //     component: SearchExpertise,
    //     props: {
    //         expertise: 'industry'
    //     },
    //     pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:search-industry-category'](':id'),
    //     name: 'search-industry-category',
    //     component: SearchExpertiseCategory,
    //     props: {
    //          expertise: 'industry'
    //     },
    //     pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:search-positions'](),
    //     name: 'search-positions',
    //     component: SearchExpertise,
    //     props: {
    //         expertise: 'positions'
    //     },
    //     pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:search-positions-category'](':id'),
    //     name: 'search-positions-category',
    //     component: SearchExpertiseCategory,
    //     props: {
    //          expertise: 'positions'
    //     },
    //     pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:search-classes'](),
    //     name: 'search-classes',
    //     component: SearchExpertise,
    //     props: {
    //         expertise: 'classes'
    //     },
    //     pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:search-classes-category'](':id'),
    //     name: 'search-classes-category',
    //     component: SearchExpertiseCategory,
    //     props: {
    //          expertise: 'classes'
    //     },
    //     pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:search-global'](),
    //     name: 'search-global',
    //     component: SearchExpertise,
    //     props: {
    //         expertise: 'global'
    //     },
    //     pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:search-global-category'](':id'),
    //     name: 'search-global-category',
    //     component: SearchExpertiseCategory,
    //     props: {
    //          expertise: 'global'
    //     },
    //     pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:search-placements'](),
    //     name: 'search-placements',
    //     component: SearchRecentPlacements,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:search-description'](),
    //     name: 'search-description',
    //     component: SearchPositions,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:search-description-position'](':id'),
    //     name: 'search-description-position',
    //     component: SeachPositionsItem,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:technologies'](),
    //     name: 'technologies',
    //     component: TechnologiesOverview,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
    // {
    //     path: Urls['control:development'](),
    //     name: 'development',
    //     component: DevelopmentOverview,
    //     props: true, pathToRegexpOptions: {strict: true}
    // },
];

const router = new VueRouter({
    //base: '/control/',
    mode: 'history',
    routes: routes,
    scrollBehavior (to, from, savedPosition) {
        return savedPosition || { x: 0, y: 0 }
    }
});
window.router = router;

router.afterEach(mixins.DocumentTitleMixin__updateTitle);

export {router, routes};
