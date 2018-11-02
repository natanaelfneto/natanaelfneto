<template>
    <div
        id="cp-published"
        class="news-v3 bg-color-white mb-4">
        
        <div class="news-v3-in">
            <ul class="list-inline d-flex">
                <li class="mr-auto">
                    <div>
                        <span>{{ item.year }}</span>
                        <span class="mx-2">-</span>
                        <span>{{ item.type }}</span>
                    </div>
                </li>
                <li class="ml-auto">
                    <a v-bind:href="item.periodic.link" target="_blank">
                        <span v-if="item.periodic.register.type == 'issn'">ISSN: {{ item.periodic.register.value }}</span>
                        <span v-if="item.periodic.register.type == 'isbn'">ISBN: {{ item.periodic.register.value }}</span>
                    </a>
                </li>
            </ul> 
            <h3>{{ item.title }}</h3>
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