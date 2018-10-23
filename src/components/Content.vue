<template>
    <div
        id="cp-content"
        class="news-v3 bg-color-white mb-4">
        
        <!-- <img class="img-responsive full-width" src="assets/img/image_01.jpg" alt=""> -->
        <div class="news-v3-in">
            <ul class="list-inline d-flex">
                <li class="mr-auto">
                    <div v-if="experience.year.start != experience.year.end">
                        <span>{{ experience.year.start }}</span>
                        <span class="px-2">-</span>
                        <span>{{ experience.year.end }}</span>
                    </div>
                    <div v-if="experience.year.start == experience.year.end">
                        <span>{{ experience.year.start }}</span>
                    </div>
                </li>
                <li class="ml-auto">
                    <a href="#" class="item">{{ experience.location }}
                        <i aria-hidden="true" class="icon-pointer"></i>
                    </a>
                </li>
            </ul>
            <h3>{{ experience.position }}</h3>
            <p>{{ experience.description }}</p>
            <div class="row px-0 mx-0">
                <ul class="post-shares col-md-4 my-0">
                    <li class="mr-auto">
                        <a href="#">
                            <i 
                                data-toggle="tooltip"
                                data-placement="bottom" 
                                v-bind:title="experience.place.name"
                                v-bind:style="{ 'background-image': 'url(' + experience.place.image.icon + ')' }">
                            </i>
                        </a>
                    </li>
                    <li class="mr-auto" v-for="parent in experience.place.parents">
                        <a href="#">
                            <i
                                data-toggle="tooltip"
                                data-placement="bottom" 
                                v-bind:title="parent.name"
                                v-bind:style="{ 'background-image': 'url(' + parent.image.icon + ')' }">
                            </i>
                        </a>
                    </li>
                </ul>
                <ul class="list-inline d-flex col-md-8 my-auto">
                    <li class="ml-auto">
                        <div v-if="experience.place.acronym != ''">
                            <span>
                                <a v-bind:href="experience.place.page_url" target="_blank">{{ experience.place.name }}</a>
                            </span>
                            <span class="px-2">-</span>
                            <span>{{ experience.place.acronym }}</span>
                        </div>
                        <div v-if="experience.place.acronym == ''">
                            <span>
                                <a v-bind:href="experience.place.page_url" target="_blank">{{ experience.place.name }}</a>
                            </span>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
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
            },
            experience: {
                type: Object,
                required: true
            }
        },
        methods: {
        }
    }
</script>

<style>
    .test {
        background-size: 100%;
    }
</style>