<template>
    <div id="component-natanaelfneto-jumbotron">
        <div class="text-white rounded bg-dark">
            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                <ol class="carousel-indicators">
                    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                </ol>
                <div class="carousel-inner">

                    <div class="carousel-item active">
                        <div class="jumbotron p-3 p-md-5 text-white rounded bg-dark align-middle d-table-row">
                            <img class="d-block custom-size" src="../../../../assets/image/bg-gyn.png" style="" alt="First slide">
                            <div class="carousel-caption px-0">
                                <h1 class="display-4 font-italic">{{ data.resume.sumary.position.major }}</h1>
                                <p class="lead my-3 d-none d-md-block">{{ data.resume.sumary.content }}</p>
                                <p class="lead mb-0">
                                    <a href="#" class="text-white">{{ data.resume.sumary.position.minor }}</a>
                                </p>
                            </div>
                        </div>
                    </div>

                    <div class="carousel-item">
                        <div class="jumbotron p-3 p-md-5 text-white rounded bg-dark align-middle d-table-row">
                            <img class="d-block custom-size" src="../../../../assets/image/bg-gyn.png" style="" alt="Second slide">
                            <div class="carousel-caption px-0">
                                <h1 class="display-4 font-italic">Title of a longer featured post</h1>
                                <p class="lead my-3 d-none d-md-block">Multiple lines of text that form the lede, informing new readers quickly and efficiently about what's most interesting in this post's contents.</p>
                                <p class="lead mb-0">
                                    <a href="#" class="text-white">Continue reading...</a>
                                </p>
                            </div>
                        </div>
                    </div>

                    <div class="carousel-item">
                        <div class="jumbotron p-3 p-md-5 text-white rounded bg-dark align-middle d-table-row">
                            <img class="d-block custom-size" src="../../../../assets/image/bg-gyn.png" alt="Third slide">
                            <div class="carousel-caption px-0">
                                <h1 class="display-4 font-italic">Title of a longer featured post</h1>
                                <p class="lead my-3 d-none d-md-block">Multiple lines of text that form the lede, informing new readers quickly and efficiently about what's most interesting in this post's contents.</p>
                                <p class="lead mb-0">
                                    <a href="#" class="text-white">Continue reading...</a>
                                </p>
                            </div>
                        </div>
                    </div>
                    
                </div>
                <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only"></span>
                </a>
                <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only"></span>
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
    .menu-btn, .menu-close {
        position: relative;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        cursor: pointer;
        transition-duration: 0.3s;
        animation: pop-btn 0.3s both ease-in-out 0.5s;
    }
    .menu-btn {
        background-color: #abc;
        z-index: 0;
        left: 12rem;
    }
    .menu-close {
        background-color: #cba;
        z-index: -1;
        left: 8.6rem;
    }
    .menu-btn > span {
        color: #222;
        font-size: x-large;
        font-weight: bold;
    }
    .menu-close > span {
        color: crimson;
        font-size: x-large;
        font-weight: bold;
    }
    @keyframes pop-btn {
        0% {
            transform: scale(0);
        }
        80% {
            transform: scale(1.2);
        }
        100% {
            transform: scale(1);
        }
    }
    .menu-btn:hover, .menu-close:hover {
        box-shadow: 0 0 0 5px rgba(170, 187, 204, 0.5);
    }
    .menu-btn:focus,
    .menu-close:focus {
        z-index: -1;
    }
    button:focus,
    button:active,
    button:focus-within,
    button:hover,
    button:visited {
        outline: none;
    }
    .menu-btn:focus ~ .menu-close {
        z-index: 0;
    }
    .menu-close:focus ~ .menu-btn {
        z-index: 0;
    }
    /* @natanaelfneto */
    .display-4 {
        font-size: 1.5rem;
    }
    .lead {
        font-size: 1rem;
    }
    .lead a {
        font-weight: normal;
    }
    .custom-size {
        min-height: 11rem;
        width: 160%;
        position: relative;
        left: -30%;
    }
    @media (min-width: 425px) {
        .custom-size {
            min-height: 13rem;
            width: 160%;
            position: relative;
            left: -30%;
        }
    }
    @media (min-width: 768px) {
        .display-4 {
            font-size: 2rem;
        }
        .lead a {
            font-weight: bold;
        }
        .custom-size {
            min-height: 20rem;
            width: 140%;
            position: relative;
            left: -20%;
        }
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
    /* */
    .menu-box {
        width: 150px;
        height: 150px;
        opacity: 0;
        border-radius: 50%;
        background-color: transparent;
        position: absolute;
        top: 50%;
        right: -40%;
        transform: translate(-50%, -50%);
        transition-duration: 0.3s;
        z-index: -1;
    }
    .menu-box i {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background-color: #ececec;
        font-size: 26px;
        color: black;
        text-align: center;
        line-height: 50px;
        position: absolute;
        left: 18px;
        top: calc(75px - 50px/2);
        box-shadow: 0 0 0.5rem #babbbc;
        transition-duration: 0.3s;
    }
    .menu-btn:focus ~ .menu-box {
        opacity: 1;
        z-index: 1;
    }
    .menu-box i:hover {
        transition-delay: initial !important;
        box-shadow: 0 0 0 5px #babbbc;
    }
    .menu-btn:focus ~ .menu-box i:nth-of-type(1) {
        transform: rotate(-90deg) translateX(85px) translateY(-50px) rotate(90deg);
        transition-delay: 0s;
    }
    /* Resumé */
    .bg-img {
        background-image: url('../../../../assets/image/bg-gyn.png');
    }
    .avatar {
        background-image: url('../../../../assets/image/profile.png');
        background-size: 100%;
        background-position: center;
        border: 1px solid #4f6984;
        border-radius: 10rem;
        background-color: pink;
        margin-left: auto;
        margin-bottom: -8rem;
        margin-right: auto;
    }
    .avatar-size {
        width: 11rem;
        height: 11rem;
    }
    @media (min-width: 1024px) {
        .avatar-size {
            width: 15rem;
            height: 15rem;
        }
    }
</style>

