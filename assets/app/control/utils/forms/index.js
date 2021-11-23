import Vue from 'vue'
import cloneDeep from "lodash/cloneDeep";
import isEqual from "lodash/isEqual";
import EditableForm from './EditableForm.vue';

function newPromise() {
    return new Promise((r) => {
        r()
    });
}

export default {
    components: {
        EditableForm
    },
    data: function () {
        return {
            data: {},
            //initialData: {},
            formState: {
                dirty: false,
                saving: false,
                showErrors: false
            }
        };
    },
    methods: {
        formsOnFetch(data) {
            this.data = data;
            this.initialData = cloneDeep(data);
            this.formState.dirty = false;
        },
        formsOnChange() {
            this.formState.dirty = !isEqual(this.data, this.initialData);
        },
        formsShowErrors() {
            this.formState.showErrors = true;
            setTimeout(() => {
                let errors = $('.u-ErrorView', this.$el);
                if (errors.length > 0) {
                    errors[0].scrollIntoView({behavior: 'smooth'});
                }
            }, 1)
        },
        formsOnSave() {
            this.$v && this.$v.$touch();
            if (this.$v && this.$v.$invalid) {
                this.formsShowErrors();
            } else {
                this.formState.saving = true;
                (this.save() || newPromise())
                    .then(() => {
                        this.formState.saving = false;
                    })
                    .catch(() => {
                        this.formState.saving = false;
                    })
            }
        },
        formsOnCancel() {
            this.data = cloneDeep(this.initialData);
            this.formState.dirty = false;
            this.cancel();
        },
        save() {
            return new Promise(function (r) {
                r();
            });
        },
        cancel() {
        },
    },
    watch: {
        data: {
            handler: function (newValue) {
                console.log('data changed');
                this.formsOnChange();
            },
            deep: true
        }
    },
    beforeRouteLeave(to, from, next) {
        console.log('beforeRouteLeave', this);
        if (!this.formState.dirty || confirm('Do you really want to leave? you have unsaved changes!')) {
            next()
        } else {
            next(false)
        }
    },
    beforeRouteUpdate(to, from, next) {
        console.log('beforeRouteUpdate', this);
        if (!this.formState.dirty || confirm('Do you really want to leave? you have unsaved changes!')) {
            next()
        } else {
            next(false)
        }
    }
};


export const StateFormsMixin = {
    components: {
        EditableForm
    },
    data: function () {
        return {
            data: {},
            //initialData: {},
            formState: {
                dirty: false,
                saving: false,
                showErrors: false
            }
        };
    },
    methods: {
        formsOnFetch(data) {
            this.data = cloneDeep(data);
            //this.initialData = cloneDeep(data);
            this.formState.dirty = false;
        },
        formsOnChange() {
            this.formState.dirty = !isEqual(this.data, this.initialData);
        },
        formsShowErrors() {
            this.formState.showErrors = true;
            setTimeout(() => {
                let errors = $('.u-ErrorView', this.$el);
                if (errors.length > 0) {
                    errors[0].scrollIntoView({behavior: 'smooth'});
                }
            }, 1)
        },
        formsOnSave() {
            this.$v && this.$v.$touch();
            if (this.$v && this.$v.$invalid) {
                this.formsShowErrors();
            } else {
                this.formState.saving = true;
                (this.save() || newPromise())
                    .then(() => {
                        this.formState.saving = false;
                    })
                    .catch(() => {
                        this.formState.saving = false;
                    })
            }
        },
        formsOnCancel() {
            this.data = cloneDeep(this.initialData);
            this.formState.dirty = false;
            this.cancel();
        },
        save() {
            return new Promise(function (r) {
                r();
            });
        },
        cancel() {
        }
    },
    watch: {
        data: {
            handler: function (newValue) {
                console.log('data changed');
                this.formsOnChange();
            },
            deep: true
        },
        initialData() {
            this.formsOnFetch(this.initialData);
        }

    },
    beforeRouteLeave(to, from, next) {
        console.log('beforeRouteLeave', this);
        if (!this.formState.dirty || confirm('Do you really want to leave? you have unsaved changes!')) {
            next()
        } else {
            next(false)
        }
    },
    beforeRouteUpdate(to, from, next) {
        console.log('beforeRouteUpdate', this);
        if (!this.formState.dirty || confirm('Do you really want to leave? you have unsaved changes!')) {
            next()
        } else {
            next(false)
        }
    }
};
