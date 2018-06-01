<template>
    <div id="component-natanaelfneto">
        <Jumbotron :data="data"></Jumbotron>
        <div id="last-blog-post-demo" class="mt-3 mt-md-5">
            <h1 class="mx-auto text-center">{{ data.posts[0].title }}</h1>
            <div class="px-1 mx-auto text-center font-weight-light font-italic">
                <span>posted by</span>
                <span class="font-weight-normal">@natanaelfneto</span>
                <span>at</span>
                <span class="font-weight-normal">10:26 PM</span>
                <span>on</span>
                <span class="font-weight-normal">May 31, 2018</span>
            </div>
            <hr/>
            <div class="px-1 px-md-5 py-2">
                <p class="px-1 px-md-5">{{ data.posts[0].content.full }}</p>
            </div>
        </div>
    </div>
</template>

<script>
    import Jumbotron from './natanaelfneto/Jumbotron.vue'

    export default {
        components: {
            Jumbotron,
        },
        props: {
            data: {
                type: Object,
                required: true
            }
        },
    }
</script>