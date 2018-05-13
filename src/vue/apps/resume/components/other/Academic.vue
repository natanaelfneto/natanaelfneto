<template>
    <div class="col-md-10 ml-auto mr-auto resume pb-0">
        <Title :title="academics.title"></Title>
        <div class="row text-center mb-4" v-for="degree in academics.degrees">
            <div class="col-md-4 mt-auto mb-auto">
                <img class="mb-1" src="../assets/image/academic-1.png" width="50%"/>
            </div>
            <div class="col-md-7 text-left academic-content">
                <span class="academic-year">{{ degree.year }}</span>
                <span class="academic-degree">
                    {{ degree.level }} <span class="font-weight-normal font-italic">in</span> {{ degree.name }}
                </span>
                <div>{{ degree.department }}<div>
                <div>{{ degree.school.name }} - {{ degree.school.acronym }}</div>
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
            academics: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>
    .academic-year {
        color: #818181;
        font-weight: 600;
    }
    .academic-degree {
        font-weight: 500;
    }
</style>