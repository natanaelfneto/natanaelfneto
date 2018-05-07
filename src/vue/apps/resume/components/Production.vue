<template>
    <div class="col-md-10 ml-auto mr-auto resume pb-0">
        <Title :title="productions.title"></Title>
        <div class="row text-center mb-4" v-for="production in productions.productions">
            <div class="col-md-4 mt-auto mb-auto">
                <img class="mb-1" src="../assets/image/production-1.png" width="50%"/>
            </div>
            <div class="col-md-7 text-left">
                <span class="production-year">{{ production.year }}</span>
                <span class="font-italic">{{ production.type }}</span>
                <div class="production-name">{{ production.name }}</div>
                <div>{{ production.institution.name }}</div>
                <p class="font-italic font-weight-light mt-2">{{ production.description }}</p>
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
            productions: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>
    .production-year {
        color: #818181;
        font-weight: 600;
    }
    .production-name {
        font-weight: 500;
    }
</style>