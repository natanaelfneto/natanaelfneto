<template>
    <div id="component-github">
        <Jumbotron :data="data"></Jumbotron>
    </div>
</template>

<script>
    import Jumbotron from './Github/Jumbotron.vue'

    export default {
        components: {
            Jumbotron,
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
</style>