<template>
    <div id="component-resume-sumary">
        {{ data.resume.sumary.content }}
    </div>
</template>

<script>
    export default {
        props: {
            data: {
                type: Object,
                required: true
            }
        },
    }
</script>