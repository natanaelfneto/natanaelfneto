<template>
    <div id="app-client-index">

        <!-- Index Head -->
		<Breadcrumbs :data="data"></Breadcrumbs>

        <!-- Index Body -->
		<div class="bg-color-light">
			<div class="container content-sm">
				<div class="row">

                    <!-- Index Body Sidebar -->
					<div class="col-md-3">
                        <Sidebar :data="data"></Sidebar>
					</div>

                    <!-- Index Body Content -->
					<div class="col-md-9">
                        <Content :data="data"></Content>
					</div>

				</div>
			</div>
		</div>

        <!-- Index Footer -->
        <Footer :data="data"></Footer>

    </div>
</template>

<script>
    import Breadcrumbs from '../../components/Breadcrumbs.vue'
    import Content from '../../components/Content.vue'
    import Footer from '../../components/Footer.vue'
    import Sidebar from '../../components/Sidebar.vue'

    export default {
        name: "Index",
        components: {
            Breadcrumbs,
            Content,
            Footer,
            Sidebar
        },
        props: {
            data: {
                type: Object,
                required: true
            }
        },
        methods: {
        },
    }
</script>

<style>
</style>