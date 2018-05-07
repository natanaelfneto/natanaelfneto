<template>
    <div class="mb-4">
        <div class="nav-scroller py-1 mb-2">
            <nav class="nav d-flex justify-content-between">
                <a class="p-2 text-muted" target="_blank" :href="link.destiny" v-for="link in navlinks">{{ link.string }}</a>
            </nav>
        </div>
        <div class="jumbotron p-3 p-md-5 text-white bg-img">
            <div class="col-md-6 m-auto text-center align-middle">
                <h1 class="display-4 font-italic">{{ position }}</h1>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            position: {
                type: String,
                required: true
            },
            navlinks: {
                type: Array,
                required: true,
            }
        }
    }
</script>

<style scoped>
    .bg-img {
        background-image: url('../assets/image/bg-gyn.png');
        height: 20rem;
        background-size: 100% 100%;
        display: flex;
        margin-bottom: 0;
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 0;
    }
    @media only screen and (max-width: 1024px) and (min-width: 768px) {
        .bg-img {
        height: 14rem;
        }
    }
    @media only screen and (max-width: 768px) and (min-width: 460px) {
        .bg-img {
        height: 14rem;
        }
    }
    @media only screen and (max-width: 460px) {
        .bg-img {
            height: 10rem;
        }
    }
    .display-4 {
        font-size: 2.5rem;
    }
    @media (min-width: 768px) {
        .display-4 {
        font-size: 2.2rem;
        }
    }
    .nav-scroller {
        position: relative;
        z-index: 2;
        height: 2.75rem;
        overflow-y: hidden;
    }
    .nav-scroller .nav {
        display: -ms-flexbox;
        display: flex;
        -ms-flex-wrap: nowrap;
        flex-wrap: nowrap;
        padding-bottom: 1rem;
        margin-top: -1px;
        overflow-x: auto;
        text-align: center;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
    }
    .nav-scroller .nav-link {
        padding-top: .75rem;
        padding-bottom: .75rem;
        font-size: .875rem;
    }
</style>