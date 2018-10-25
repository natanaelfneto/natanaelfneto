<template>
    <div
        id="cp-published"
        class="news-v3 bg-color-white mb-4">
        
        <div class="news-v3-in">
            <ul class="list-inline d-flex">
                <li class="mr-auto">
                    <div>
                        <span>{{ item.year }}</span>
                        <span v-if="item.location.is.sn != '' || item.location.is.bn != ''">
                            <span>{{ item.location.name }}</span>
                        </span>
                    </div>
                </li>
                <li class="ml-auto">
                    <a v-bind:href="item.location.link" target="_blank">
                        <span v-if="item.location.is.sn == '' && item.location.is.bn == ''">
                            <span>{{ item.location.name }}</span>
                        </span>
                        <span v-if="item.location.is.sn != ''">ISSN: {{ item.location.is.sn }}</span>
                        <span v-if="item.location.is.bn != ''">ISBN: {{ item.location.is.bn }}</span>
                    </a>
                </li>
            </ul>
            <h3>{{ item.work }}</h3>
            <img 
                v-if="item.preview != ''"
                class="img-responsive full-width" 
                src="assets/img/bg-gyn.png" 
                alt="">
            <span class="pr-2" v-for="author in item.authors">{{ author.name }};</span>
            <p class="mb-0 mt-3">{{ item.description }}</p>
            <div class="row px-0 mx-0">
                <ul class="post-shares ml-auto my-0">
                    <li v-for="source in item.sources">
                        <a v-bind:href="source.link">
                            <i v-bind:class="source.icon" class="cp-font"></i>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        components: {
        },
        props: {
            data: {
                type: Object,
                required: true
            },
            item: {
                type: Object,
                required: true
            }
        },
        methods: {
        }
    }
</script>

<style scoped>
    .cp-font {
        font-size: 2rem !important;
    }
</style>