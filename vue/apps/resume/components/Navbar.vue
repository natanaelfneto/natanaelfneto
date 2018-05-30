<template>
    <div id="component-navbar">
        <header class="blog-header py-1 py-sm-3">
            <div class="flex-nowrap justify-content-between align-items-center d-none d-md-block">
                <div class="row">
                    <!-- START: Language Selector -->
                    <div class="col-md-4 col-sm-12 py-1 my-auto">
                        <LanguageSelector :data="data"></LanguageSelector>
                    </div>
                    <!-- END: Language Selector -->
                    <div class="col-md-4 col-sm-12 py-1 text-center">
                        <a class="blog-header-logo text-nowrap text-dark" href="#">{{ data.profile.name.display_name }}</a>
                    </div>
                    <div class="col-md-4 col-sm-12 d-flex justify-content-end align-items-center">
                        <a 
                            class="btn btn-sm btn-outline-secondary d-inline-flex py-2 border custom-border-color" 
                            href="#" 
                            id="dropdownSignInForm" 
                            data-toggle="dropdown"
                            aria-haspopup="true" 
                            aria-expanded="false"
                            @click="pusheenReset()">
                            <div class="item text-center mx-1">
                                <i aria-hidden="true" class="fas fa-user-astronaut"></i>
                            </div>
                            <span class="mx-1">Sign in</span>
                        </a>
                        <SignInForm :data="data"></SignInForm>
                    </div>
                </div>
            </div>
        </header>
        <nav class="navbar navbar-expand-md navbar-light rounded">
            <span class="blog-header-logo text-dark d-md-none d-lg-none d-xl-none">{{ data.profile.name.display_name }}</span>
            <button 
                id="menu-toggler-close"
                class="navbar-toggler collapsed d-md-none d-lg-none d-xl-none" 
                type="button" 
                data-toggle="collapse" 
                data-target="#navbarsExample10" 
                aria-controls="navbarsExample10" 
                aria-expanded="false" 
                aria-label="Toggle navigation">
                <span class="item-box">
                    <span class="item text-danger">
                        <span aria-hidden="true" class="icon-close"></span>
                    </span>
                </span>
            </button>
            <div class="navbar-collapse d-md-block collapse" id="navbarsExample10">
                <ul class="navbar-nav justify-content-md-between">
                    <!-- START: Language Selector -->
                    <li class="row nav-item d-inline-flex d-md-none d-lg-none d-xl-none">
                        <div class="py-2 text-muted item text-center">
                            <i aria-hidden="true" class="icon-eyeglasses"></i>
                        </div>
                        <LanguageSelector :data="data"></LanguageSelector>
                    </li>
                    <!-- END: Language Selector -->
                    <!-- START: Link Tabs -->
                    <li :id="'navbar_link_'+link.string"
                        class="row nav-item d-inline-flex"
                        v-for="link in data.links"
                        @click="setCurrentActiveTab($event)">
                        <div class="py-2 text-muted item text-center">
                            <i aria-hidden="true"
                                :class="[
                                    link.icon.class.base,
                                    link.icon.class.name,
                                    link.icon.class.custom
                                    ]">
                            </i>
                        </div>
                        <a class="py-2 text-muted" href="#">{{ link.string }}</a>
                    </li>
                    <!-- END: Link Tabs -->
                    <li class="row nav-item dropdown d-md-none d-lg-none d-xl-none">
                        <div class="py-2 text-muted item text-center">
                            <i aria-hidden="true" class="fas fa-user-astronaut"></i>
                        </div>
                        <a 
                            class="py-2 text-muted" 
                            href="#" 
                            id="dropdownSignInForm" 
                            data-toggle="dropdown" 
                            aria-haspopup="true" 
                            aria-expanded="false"
                            @click="pusheenReset()">
                            Sign in
                        </a>
                        <SignInForm :data="data"></SignInForm>
                    </li>
                </ul>
            </div>
            <button
                id="menu-toggler-open"
                class="navbar-toggler collapsed ml-auto" 
                type="button" 
                data-toggle="collapse" 
                data-target="#navbarsExample10" 
                aria-controls="navbarsExample10" 
                aria-expanded="false" 
                aria-label="Toggle navigation">
                <span class="item-box">
                    <span class="item">
                        <span aria-hidden="true" class="icon-cup"></span>
                    </span>
                </span>
            </button>
        </nav>
    </div>
</template>

<script>
    import LanguageSelector from './Navbar/LanguageSelector.vue'
    import SignInForm from './Navbar/SignInForm.vue'

    export default {
        components: {
            LanguageSelector,
            SignInForm
        },
        props: {
            data: {
                type: Object,
                required: true
            }
        },
        methods: {
            pusheenReset(){
                this.data.pusheenStatus = 'dancing';
            },
            setCurrentActiveTab(e) {
                this.data.activeTab = e.target.closest('li').id.replace('navbar_link_','');
                document.getElementById('menu-toggler-close').click();
            }
        }
    }
</script>

<style scoped>
    .fac-width {
        -webkit-text-stroke-width: 0.02rem;
    }
    .fac-color-white {
        -webkit-text-stroke-color: white;
    }
    @media (min-width: 768px) {
        .navbar-expand-md .navbar-collapse {
            display: unset !important;
        }
        .blog-header {
            line-height: 1;
            border-bottom: 1px solid #e5e5e5;
        }
        .blog-header-logo {
            line-height: unset !important;
            font-family: "Playfair Display", Georgia, "Times New Roman", serif;
            font-size: 2.25rem;
        }
        .blog-header-logo:hover {
            text-decoration: none;
        }
    }
    .blog-header-logo {
        line-height: 2;
        font-family: "Playfair Display", Georgia, "Times New Roman", serif;
        font-size: 1.5rem;
    }
    #menu-toggler-open[aria-expanded=true] {
        width: 100%;
        border-radius: 0;
        border-top: 1px solid #e5e5e5;
        padding-bottom: 0px;
        padding-top: 0.75rem;
        margin-top: 0.75rem;
    }
    #menu-toggler-open[aria-expanded=true] span[class=item]{
        font-size: 2rem;
    }
    .navbar-toggler {
        border: 0;
    }
    button:focus,
    .btn-outline-secondary:focus, 
    .btn-outline-secondary:not(:disabled):not(.disabled):active:focus {
        outline: none;
        box-shadow: unset;
    }
    .nav-item>.item {
        min-width: 2rem;
    }
    #menu-toggler-close {
        display: none;
    }
    #menu-toggler-close[aria-expanded=true] {
        display: inline-block;
    }
    .custom-border-color {
        border-color: #e5e5e5;
    }
    #navbarsExample10 {
        margin-left: -20px;
        margin-right: -20px;
    }
    #navbarsExample10>ul {
        margin-left: 20px;
        margin-right: 20px;
    }
</style>