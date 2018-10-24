<template>
    <div id="cp-sidebar-left">

        <Academic :data="data"></Academic>

        <Github :data="data"></Github>

        <div class="headline-v2"><h2>Newsletter</h2></div>
        <!-- Blog Newsletter -->
        <div class="blog-newsletter">
            <p>Subscribe to our newsletter for good news, sent out every month.</p>
            <div class="input-group">
                <input type="text" class="form-control" placeholder="Email">
                <span class="input-group-btn">
                    <button class="btn-u" type="button">Subscribe</button>
                </span>
            </div>
        </div>
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