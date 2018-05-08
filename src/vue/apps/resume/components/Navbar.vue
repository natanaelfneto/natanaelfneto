<template>
    <header class="blog-header py-3">
        <div class="row flex-nowrap justify-content-between align-items-center">
            <div class="col-4 pt-1">
                <a class="text-muted" href="#" @click="callFloatMenu($event, lang.available)">
                    <span>Language {{ getSettedLanguage() }}</span>
                </a>
            </div>
            <div class="col-4 text-center">
                <a class="blog-header-logo text-dark" href="#">Natanael F. Neto</a>
            </div>
            <div class="col-4 d-flex justify-content-end align-items-center">
                <a class="text-muted mr-3" href="#">
                    <span class="item">
				        <span aria-hidden="true" class="icon-magnifier"></span>
				    </span>
                </a>
                <a class="btn btn-sm btn-outline-secondary" href="#">Login</a>
            </div>
        </div>
    </header>
</template>

<script>
    export default {
        props: {
            lang: {
                type: Object,
                required: true
            },
        },
        methods: {
            getSettedLanguage() {
                var available = this.lang.available;
                var setted = this.lang.setted;
                var index = available.map(function(e) { return e.tag; }).indexOf(setted);
                return available[index].own_escription;
            },
            callFloatMenu(e, options) {
                e.stopPropagation()
                var longest = options.reduce(
                    (a, b) => { return a.en_description.length > b.en_description.length ? a : b }
                ).en_description.length
                var floatMenu = {
                    isFloatMenu: true,
                    visible: true,
                    fixed: true,
                    sourceParams: {
                        x: e.target.getBoundingClientRect().x,
                        y: e.target.getBoundingClientRect().y,
                        width: e.target.getBoundingClientRect().width,
                        height: e.target.getBoundingClientRect().height,
                    },
                    floatParams: {
                        x:e.clientX,
                        y:e.clientY,
                        width: e.target.getBoundingClientRect().width + longest,
                        height:''
                    },
                    options: options.map(function(e) { return e.en_description; })
                }
                this.$emit('updateFloatMenuPosition',floatMenu)
            }
        }
    }
</script>

<style scoped>
    .blog-header {
        line-height: 1;
        border-bottom: 1px solid #e5e5e5;
    }
    .blog-header-logo {
        font-family: "Playfair Display", Georgia, "Times New Roman", serif;
        font-size: 2.25rem;
    }
    .blog-header-logo:hover {
        text-decoration: none;
    }
</style>