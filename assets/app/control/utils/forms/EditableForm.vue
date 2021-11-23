<template>
    <div class="EditableForm" :class="{'u-ShowErrors': formState.showErrors}">
        <slot></slot>
        <save-view :show="formState.dirty" :saving="formState.saving" @save="onSave" @cancel="onCancel"></save-view>
    </div>
</template>

<script>
    export default {
        name: "EditableForm",
        props: {
            formState: Object,
            onCancel: Function,
            onSave: Function,
        }
    };
</script>

<style scoped lang="less">
    @import "~styles/const.less";
</style>