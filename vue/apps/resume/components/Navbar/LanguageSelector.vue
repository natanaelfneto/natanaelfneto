<template>
    <div id="component-navbar-language-selector" class="my-auto">
        <span class="py-2 text-muted" href="#">Language:</span>
        <span class="dropdown">
            <span class="py-2" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <a class="text-muted mx-1" href="#">
                    {{ getSettedLanguageProps(data.languages.setted).own_description }}
                </a>
                <span 
                    aria-hidden="true" 
                    class="flag-icon"
                    data-toggle="tooltip" 
                    data-placement="bottom"
                    :title="getSettedLanguageProps(data.languages.setted).own_country"
                    :class="'flag-icon-' + getSettedLanguageProps(data.languages.setted).country_tag">
                </span>
            </span>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <a 
                    class="dropdown-item" 
                    href="#" 
                    v-for="language in data.languages.available"
                    :class="returnIfLanguageMatchSetted(language,'disabled')"
                    @click="setSettedLanguage(language.language_tag + '-' + language.country_tag)">
                    <span 
                        aria-hidden="true" 
                        class="flag-icon"
                        data-toggle="tooltip" 
                        data-placement="bottom"
                        :title="language.own_country"
                        :class="'flag-icon-' + language.country_tag"
                        :style="returnIfLanguageMatchSetted(language,{ filter:'grayscale(100%)' })">
                    </span>
                    <span class="mx-2">{{ language.own_description }}</span>
                </a>  
            </div>
        </span>
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
        methods: {
            getSettedLanguageProps(settedLanguage) {
                return this.data.languages.available.find(
                    language => language.language_tag + '-' + language.country_tag === settedLanguage
                );
            },
            returnIfLanguageMatchSetted(language,return_this) {
                if(this.data.languages.setted == language.language_tag + '-' + language.country_tag) {
                    return return_this;
                } else { return; }
            },
            setSettedLanguage(languageAndCountryTags) {
                this.data.languages.setted = languageAndCountryTags;
            }
        }
    }
</script>

<style scoped>
    .dropdown > [type=button] {
        -webkit-appearance: unset;
    }
</style>