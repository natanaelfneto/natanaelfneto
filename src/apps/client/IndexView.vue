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
                        <ul class="nav nav-pills mb-3" id="ContentTab" role="tablist">
                            <li class="nav-item">
                                <a 
                                    class="nav-link bg-fade-blue active" 
                                    id="resume-tab" 
                                    data-toggle="tab" 
                                    href="#resume" 
                                    role="tab" 
                                    aria-controls="resume" 
                                    aria-selected="true">
                                    Resumé
                                </a>
                            </li>
                            <li class="nav-item">
                                <a 
                                    class="nav-link bg-fade-blue" 
                                    id="published-tab" 
                                    data-toggle="tab" 
                                    href="#published" 
                                    role="tab" 
                                    aria-controls="published" 
                                    aria-selected="false">
                                    Publicações
                                </a>
                            </li>
                        </ul>
                        <div class="tab-content" id="myTabContent">
                            <div 
                                class="tab-pane fade show active" 
                                id="resume" 
                                role="tabpanel" 
                                aria-labelledby="resume-tab">
                                <component
                                    :is="data.activeTab"
                                    :data="data"
                                    :item="item"
                                    v-for="item in data.experiences">>
                                </component>
                            </div>
                            <div 
                                class="tab-pane fade" 
                                id="published" 
                                role="tabpanel" 
                                aria-labelledby="published-tab">
                                <component
                                    :is="data.activeTab"
                                    :data="data"
                                    :item="item"
                                    v-for="item in data.published">>
                                </component>
                            </div>
                        </div>
                        
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
    import Footer from '../../components/Footer.vue'
    import Published from '../../components/Published.vue'
    import Resume from '../../components/Resume.vue'
    import Sidebar from '../../components/Sidebar.vue'

    export default {
        name: "Index",
        components: {
            Breadcrumbs,
            Footer,
            Published,
            Resume,
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

<style scoped>
    .bg-fade-blue.active {
        background-color: var(--first-color) !important;
    }
    .nav-tabs .nav-link {
        border-bottom-color: #dee2e6;
    }
</style>