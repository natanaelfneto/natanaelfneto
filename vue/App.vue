<template>
    <component :is="selectedMainApp"></component>
</template>

<script>
    import PersonalPage from './apps/resume/PersonalPage.vue'

    export default {
        components: {
            PersonalPage
        },
        data: function() {
            return {
                selectedMainApp: 'PersonalPage'
            }
        }
    }
</script>