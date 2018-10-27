<template>
    <div id="cp-sidebar-left">
        
        <Academic v-if="data.sidebar.academic.is_enabled" :data="data"></Academic>

        <Github v-if="data.sidebar.github.is_enabled" :data="data"></Github>
        
    </div>
</template>

<script>
    import Academic from './Academic.vue'
    import Github from './Github.vue'

    export default {
        components: {
            Academic,
            Github
        },
        props: {
            data: {
                type: Object,
                required: true
            }
        },
        methods: {
            clipboardCopy: function(url) {
                let CopiedObject = document.createElement("textarea");
                try {
                    CopiedObject.value = 'git clone '+url
                    CopiedObject.setAttribute('readonly', '');
                    document.body.appendChild(CopiedObject);
                    CopiedObject.select()
                    document.execCommand('copy');
                    document.body.removeChild(CopiedObject);
                } catch (err) {
                    console.log("Element value could not be copied")
                }
            },
        }
    }
</script>

<style>
</style>