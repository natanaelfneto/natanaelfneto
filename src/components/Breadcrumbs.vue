<template>
    <div 
        id="cp-breadcrumbs" 
        class="breadcrumbs-v1"
        v-bind:style="{ 'background-image': 'url(' + data.background_image + ')' }">
        
        <div class="container">
            <div
                class="cp-avatar"
                v-bind:style="{ 'background-image': 'url(' + data.profile_image + ')' }">
            </div>
            <div class="cp-text">
                <h1><small>Natanael F. Neto</small></h1>
                <span>Electrical and Software Engineer</span>
            </div>
        </div>

    </div>
</template>

<script>
    export default {
        components: {
        },
        props: {
            data: {
                type: Object,
                required: true
            }
        },
        methods: {
        }
    }
</script>

<style>
    .cp-text {
        margin-left: 15rem;
        position: relative;
        top: 5rem;
    }
    .cp-avatar {
        width: 12rem;
        height: 12rem;
        background-size: 100%;
        border: 1px solid;
        border-radius: 10rem;
        margin-right: auto;
        margin-bottom: -15rem;
    }
</style>