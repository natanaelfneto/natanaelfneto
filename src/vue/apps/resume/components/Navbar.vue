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
                <a class="btn text-muted" href="#">
                    <span class="item"><span class="icon-magnifier"></span></span>
                </a>
                <!-- end search -->
                <!-- start login -->
                <a class="btn btn-outline-secondary" href="#">Login</a>
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
    .navbar-name {
        font-family: "Playfair Display", Georgia, "Times New Roman", serif;
        font-size: 2.25rem;
    }
    .dropdown-menu {
        left: 10px;
    }
</style>;