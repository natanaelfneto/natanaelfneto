<template>
    <div id="component-natanaelfneto">
        <Jumbotron :data="data"></Jumbotron>
    </div>
</template>

<script>
    import Jumbotron from './natanaelfneto/Jumbotron.vue'

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