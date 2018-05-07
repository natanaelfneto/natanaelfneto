<template>
    <div class="col-md-10 ml-auto mr-auto resume pb-0">
        <Title :title="knowledges.title"></Title>
        <div class="row text-center mb-4" v-for="knowledge in knowledges.knowledges">
            <div class="col-md-4 mt-auto mb-auto"></div>
            <div class="col-md-7 text-left">
                <img class="ml-1 mr-1 knowledge-image" src="../assets/image/knowledge-1.png"/>
                <span class="ml-1 mr-1">
                    <span class="font-italic text-secondary">{{ knowledge.company }}'s</span>
                    <span class="font-weight-bold">{{ knowledge.name }}</span>
                </span>
                <span v-for="version in knowledge.versions">
                    "<span class="text-info">{{ version }}</span>"
                </span>
            </div>
        </div>
    </div>
</template>

<script>
    import Title from './sub-components/Title.vue'

    export default {
        components: {
            Title
        },
        props: {
            knowledges: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>
    .knowledge-image {
        max-width: 32px;
        max-height: 32px;
    }
</style>