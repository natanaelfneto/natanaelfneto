<template>
    <div id="component-navbar-language-selector" class="my-auto">
        <a class="py-2 text-muted" href="#">Language:</a>
        <span class="py-2">
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
            }
        }
    }
</script>