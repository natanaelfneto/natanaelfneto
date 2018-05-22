<template>
    <div id="component-jumbotron">

        <div class="text-white rounded bg-dark">
            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                <ol class="carousel-indicators">
                    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                </ol>
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <div 
                            class="jumbotron p-3 p-md-5 text-white rounded bg-dark align-middle" 
                            style="display: table-row;">
                            <img class="d-block custom-size" src="../assets/image/bg-gyn.png" style="" alt="First slide">
                            <div class="carousel-caption d-none d-md-block px-0">
                                <h1 class="display-4 font-italic">Title of a longer featured post</h1>
                                <p class="lead my-3">Multiple lines of text that form the lede, informing new readers quickly and efficiently about what's most interesting in this post's contents.</p>
                                <p class="lead mb-0">
                                    <a href="#" class="text-white font-weight-bold">Continue reading...</a>
                                </p>
                            </div>
                        </div>
                    </div>
                    
                </div>
                <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </a>
                <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </a>
            </div>
        </div>

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
    }
</script>

<style scoped>
    .display-4 {
        font-size: 2rem;
    }
    .lead {
        font-size: 1rem;
    }
    .custom-size {
        min-height: 20rem;
        width: 140%;
        position: relative;
        left: -20%;
    }
    @media (min-width: 1024px) {
        .display-4 {
            font-size: 3rem;
        }
        .lead {
            font-size: 1.25rem;
        }
        .custom-size {
            min-height: 25rem;
            width: 100%;
            position: relative;
            left: 0%;
        }
    }
</style>