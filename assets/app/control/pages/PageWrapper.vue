<template>
    <div>
        <main-nav></main-nav>
        <router-view></router-view>
    </div>
</template>

<script>
import MainNav from 'components/MainNav.vue'
export default {
    name: "PageWrapper",
    components: {
        MainNav
    }
};
</script>

<style lang="less">
    @import "~styles/const.less";
    body {
        background: @color-gray;
    }
</style>