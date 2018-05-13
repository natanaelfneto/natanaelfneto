<template>
    <component :is="selectedMainApp"></component>
</template>

<script>
    import Resume from './apps/resume/Resume.vue'

    export default {
        components: {
            Resume
        },
        data: function() {
            return {
                selectedMainApp: 'Resume'
            }
        }
    }
</script>