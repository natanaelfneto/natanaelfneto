<template>
    <div class="row text-center mb-4">
        <div class="col-md-4 mt-auto mb-auto"></div>
        <div class="col-md-7 text-left">
            <h1 class="resume-title">{{ title }}</h1>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            title: {
                type: String,
                required: true
            }
        }
    }
</script>