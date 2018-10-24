<template>
    <div id="cp-academic">
        <div class="headline-v2"><h2>Formação Acadêmica</h2></div>
        <ul class="list-unstyled blog-trending margin-bottom-50">
            <li v-for="degree in data.academic">
                <h3>
                    <span class="badge badge-secondary">{{ degree.acronym }}</span>
                    <a href="#">{{ degree.title }}</a></h3>
                <small class="d-block">{{ degree.department }}</small>
                <small>
                    <b>{{ degree.year.end }}</b>
                    <div class="d-inline pl-1">{{ degree.institution }}</div>
                </small>
            </li>
        </ul>
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
</style>