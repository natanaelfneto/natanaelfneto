<template>
    <div id="component-resume-fieldset" class="mx-lg-5 px-md-5">
    <div
        class="pb-2 mb-3"
        style="border-radius: 1px; background-color: #e9ecef4f; box-shadow: rgba(0, 0, 0, 0.35) 0.1rem 0.1rem .5em 0.1rem !important"
        v-for="(fieldset, index, i) in data.resume" 
        v-if="fieldset.isActive"
        :class="i == 0 ? 'pt-5' : 'pt-3'">
        <div class="row mt-4 mt-md-0">
            <div class="col-md-6 py-1 mr-auto">
                <h3 class="mb-0 mx-5">
                    <a class="text-dark text-sm-nowrap" href="#">
                        {{ fieldset.title }}
                    </a>
                </h3>
            </div>
            <div class="col-md-6"></div>
            <div class="offset-1 col-10 p-2 m-auto">
                <p class="card-text mb-auto">
                    <component :is="fieldset.title.replace(' ','')" :data="data"></component>
                </p>
            </div>
        </div>
    </div>
    </div>
</template>

<script>
    import Sumary from './ResumeFieldset/Sumary.vue'
    import AcademicFormation from './ResumeFieldset/AcademicFormation.vue'

    export default {
        components: {
            Sumary,
            AcademicFormation
        },
        props: {
            data: {
                type: Object,
                required: true
            }
        },
    }
</script>

<style scoped>
    .text-sm-nowrap {
        white-space: unset !important;
    }
    @media (min-width: 768px) {
        .text-sm-nowrap {
            white-space: nowrap !important;
        }
    }
</style>