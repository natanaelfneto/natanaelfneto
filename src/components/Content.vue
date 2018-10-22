<template>
    <div
        id="cp-content"
        class="news-v3 bg-color-white margin-bottom-60">
        
        <img class="img-responsive full-width" src="assets/img/image_01.jpg" alt="">
        <div class="news-v3-in">
            <ul class="list-inline posted-info">
                <li>By <a href="#">Alexander Jenni</a></li>
                <li>In <a href="#">Design</a></li>
                <li>Posted January 24, 2015</li>
            </ul>
            <h2><a href="#">Incredible standard post “IMAGE”</a></h2>
            <p>Nullam elementum tincidunt massa, a pulvinar leo ultricies ut. Ut fringilla lectus tellus, imperdiet molestie est volutpat at. Sed viverra cursus nibh, sed consectetur ipsum sollicitudin sed. Cras erat est, euismod id congue sed, sollicitudin sed odio. Nullam non metus in mi rhoncus efficitur...</p>
            <ul class="post-shares">
                <li>
                    <a href="#">
                        <i class="rounded-x icon-speech"></i>
                        <span>26</span>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <i class="rounded-x icon-share"></i>
                        <span>98</span>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <i class="rounded-x icon-heart"></i>
                        <span>30</span>
                    </a>
                </li>
            </ul>
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
            }
        },
        methods: {
        }
    }
</script>

<style>
</style>