<template>
    <header class="blog-header py-3">
        <div class="row flex-nowrap justify-content-between align-items-center">
            <div class="col-4 pt-1">
                <a class="text-muted" href="#" @click="changeContentOutside">Language (English)</a>
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
        methods: {
            changeContentOutside() {
                console.log('called')
                this.$emit('change')
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