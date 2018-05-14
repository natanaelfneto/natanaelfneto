<template>
    <header class="py-3">
        <!-- start header -->
        <div class="row align-items-center">
            <!-- start language -->
            <div class="col-3 p-2">
                <button 
                    type="button" 
                    class="btn btn-link text-muted" 
                    data-toggle="dropdown" 
                    aria-haspopup="true" 
                    aria-expanded="false">
                    Language: {{ getSettedLanguage(langs) }}
                </button>
                <div class="dropdown-menu">
                    <a class="dropdown-item disabled" href="#">
                        <span>{{ getSettedLanguage(langs) }} (active)</span>
                    </a>
                    <div class="dropdown-divider"></div>
                    <a
                        :id="'id_' + lang.tag" 
                        class="dropdown-item" 
                        href="#" 
                        @click="setLanguage($event)" 
                        v-for="(lang, index) in langs.available">
                        <span>{{ lang.en_description }}</span>
                    </a>
                </div>
            </div>
            <!-- end language -->
            <!-- start full name -->
            <div class="col-6 p-2 text-center">
                <a class="text-dark navbar-name" href="#">
                    <span>{{ profile.name.first }}</span>
                    <span>{{ profile.name.last }}</span>
                </a>
            </div>
            <!-- end full name -->
            <!-- start search/login -->
            <div class="col-3 p-2 text-right">
                <!-- start search -->
                <div class="row">
                    <div class="col-9 px-0 search-el">
                        <form class="form-inline my-2 my-lg-0">
                            <label class="item">
                                <input type="text" placeholder="Search..." class="form-control">
                                <span class="icon-magnifier"></span>
                            </label>
                        </form>
                        <!-- end search -->
                        <!-- start login -->
                    </div>
                    <div class="col-3 dropdown">
                        <button 
                            class="btn btn-outline-secondary" 
                            type="button" 
                            data-toggle="dropdown" 
                            aria-haspopup="true" 
                            aria-expanded="false">
                            Login
                        </button>
                        <form class="dropdown-menu dropdown-menu-right p-4 mt-2 login-form">
                            <div class="login-image text-center mb-2">
                                <img src="../assets/image/profile.png" />
                            </div>
                            <div class="form-group">
                                <label for="dropdownFormEmail">E-mail</label>
                                <input type="email" class="form-control" id="dropdownFormEmail" placeholder="email@example.com">
                            </div>
                            <div class="form-group">
                                <label for="dropdownFormPassword">Password</label>
                                <input type="password" class="form-control" id="dropdownFormPassword" placeholder="Password">
                            </div>
                            <div class="form-check">
                                <input type="checkbox" class="form-check-input" id="dropdownCheck">
                                <label class="form-check-label" for="dropdownCheck">
                                Remember me
                                </label>
                            </div>
                            <button type="button" class="btn btn-block btn-outline-secondary mt-2">Sign in</button>
                        </form>
                    </div>
                </div>
                <!-- end login -->
            </div>
            <!-- end search/login -->
        </div>
        <!-- end header -->
        <!-- start links -->
        <nav class="nav d-flex justify-content-between">
            <a class="p-2 text-muted" target="_blank" :href="link.destiny" v-for="link in links">
                <span>{{ link.string }}</span>
            </a>
        </nav>
        <!-- end links -->
    </header>
</template>

<script>
    export default {
        props: {
            profile: {
                type: Object,
                required: true
            },
            langs: {
                type: Object,
                required: true
            },
            links: {
                type: Array,
                required: true,
            }
        },
        methods: {
            getSettedLanguage(langs) {
                return langs.available[
                    langs.available.map(function(e) { 
                        return e.tag;
                        }).indexOf(langs.setted)
                ].own_description;
            },
            setLanguage(e) {
                if(!e.target.id.includes('id_')) {
                    var selectedLang = e.target.parentElement.id.replace(/id_/g,'');
                } else {
                    var selectedLang = e.target.id.replace(/id_/g,'');
                }
                this.langs.setted = selectedLang;
            }
        }
    }
</script>

<style scoped>
    /* navbar component */
    .navbar-name {
        font-family: "Playfair Display", Georgia, "Times New Roman", serif;
        font-size: 2.25rem;
    }
    /* login form sub component */
    .login-form {
        min-width: 20rem;
        box-shadow: 1px 2px 1px darkgrey;
    }
    .login-image {
        min-width: 100%;
        min-height: 100%;
        background-color: white;
    }
    .login-image img {
        max-width: 60%;
        border: 1px solid gray;
        border-radius: 10rem;
    }
    /* search sub component */
    .search-el {
        position: relative;
        left: 15px;
    }
    .search-el label {
        text-align: right;
        margin-left: auto;
    }
    .search-el input {
        width: 40px;
        color: transparent;
        background-color: transparent;
        border-color: #6c757d;
        -webkit-transition: all 0.5s ease 0s;
        -moz-transition: all 0.5s ease 0s;
        -o-transition: all 0.5s ease 0s;
        transition: all 0.5s ease 0s;
    }
    .search-el input::-webkit-input-placeholder {
        color: transparent;
    }
    .search-el input:focus {
        width: 150px;
        color: #6c757d;
    }
    .search-el input:focus::-webkit-input-placeholder {
        color: #6c757d;
    }
    .search-el input:focus ~ span {
        color: transparent !important;
    }
    .search-el span {
        color: #6c757d;
        position: relative;
        left: -27px;
    }
</style>