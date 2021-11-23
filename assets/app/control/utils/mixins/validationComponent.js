export default {
    props: {
    },
    computed: {

        hasError() { return this.errors && this.errors.$error },

        innerValue: {
            get() {
                if (this.value && this.value.hasOwnProperty('$model')) {
                    return this.value.$model;
                } else {
                    return this.value;
                }
            },
            set(newVal) {
                if (this.value && this.value.hasOwnProperty('$model')) {
                    this.value.$model = newVal;
                }
                else {
                    this.$emit('input', newVal);
                }
            }
        },

        errors() {
            if (this.value && this.value.hasOwnProperty('$model')) {
                return this.value;
            } else {
                return undefined;
            }
        }

    }
}
