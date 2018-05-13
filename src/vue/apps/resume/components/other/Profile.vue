<template>
    <div class="col-md-10 ml-auto mr-auto pb-0 resume">
        <Title :title="profile.title"></Title>
        <div class="row text-center mb-4">
            <div class="col-md-4 mt-auto mb-auto">
                <img class="resume-image" src="../assets/image/profile.png" width="80%"/>
            </div>
            <div class="col-md-7 text-left mt-auto mb-auto">
                <p>{{ profile.sumary }}</p>
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
            profile: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>
    
</style>