<template>
    <div>
        <Profile :profile="resume.profile"></Profile>
        <Academic :academics="resume.academics"></Academic>
        <Experience :experiences="resume.experiences"></Experience>
        <Production :productions="resume.productions"></Production>
        <Knowledge :knowledges="resume.knowledges"></TechKnowledge>
    </div>
</template>

<script>
    import Profile from './Profile.vue'
    import Academic from './Academic.vue'
    import Experience from './Experience.vue'
    import Production from './Production.vue'
    import Knowledge from './knowledge.vue'

    export default {
        components: {
            Profile,
            Academic,
            Experience,
            Production,
            Knowledge
        },
        props: {
            resume: {
                type: Object,
                required: true
            }
        }
    }
</script>