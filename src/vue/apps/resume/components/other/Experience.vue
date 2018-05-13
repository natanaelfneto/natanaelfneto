<template>
    <div class="col-md-10 ml-auto mr-auto resume pb-0">
        <Title :title="experiences.title"></Title>
        <div class="row text-center mb-4" v-for="experience in experiences.experiences">
            <div class="col-md-4 mt-auto mb-auto">
                <img class="mb-1" src="../assets/image/experience-1.png" width="50%" />
            </div>
            <div class="col-md-7 text-left">
                <span class="experience-year">{{ experience.year.start }}-{{ experience.year.end }}</span>
                <span class="font-weight-bold">{{ experience.position }}</span>
                <div class="mb-2 experience-institution">{{ experience.institution.name }} - {{ experience.institution.acronym }}</div>
                <p class="font-italic font-weight-light">{{ experience.description }}</p>
                <div class="row mt-2" v-for="reference in experience.references">
                    <div class="col-md-3 text-secondary pr-0">
                        Reference:
                    </div>
                    <div class="col-md-9 font-weight-normal">
                        <div class="font-italic">{{ reference.position }}</div>
                        <div>{{ reference.level }} {{ reference.name }}</div>
                        <div>{{ reference.email }}</div>
                        <div>{{ reference.phone }}</div>
                    </div>
                </div>
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
            experiences: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>
    .experience-year {
        color: #818181;
        font-weight: 600;
    }
    .experience-institution {
        font-weight: 500;
    }
</style>