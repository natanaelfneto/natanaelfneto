<template>
    <div id="component-github-jumbotron">
        <div class="row p-3 p-md-5 text-white rounded bg-dark mb-5 mb-md-3">
            <div class="col-md-6 px-0">
                <h1 class="display-4 font-italic">Github Profile</h1>
                <p class="lead mb-0 pr-5 mr-4 pr-md-0 mr-md-0">
                    <a href="#" class="text-white">{{ data.github.user.bio }}</a>
                </p>
                <p class="lead my-3">{{ data.github.user.login }}@github.com</p>
            </div>
            <div class="col-md-6 mt-auto">
                <div class="row mx-auto github-orgs">
                <div  class="avatar org-avatar-size mr-0 my-2 ml-auto">
                    <div class="my-2 item text-center">
                        <i aria-hidden="true" class="fab fa-github-square"></i>
                    </div>
                </div>
                    <div v-for="(org, index) in data.github.orgs"
                        class="avatar org-avatar-size mr-0 my-2"
                        :style="{ 'background-image': 'url(' + org.avatar_url + ')' }">
                    </div>
                </div>
                <div 
                    class="avatar avatar-size"
                    :style="{ 'background-image': 'url(' + data.github.user.avatar_url + ')' }">
                </div>
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
    .avatar {
        position: relative;
        top: -6rem;
        background-size: 100%;
        background-position: center;
        border: 1px solid #4f6984;
        border-radius: 10rem;
        background-color: pink;
        margin-left: auto;
        margin-bottom: -18rem;
        margin-right: auto;
    }
    .avatar > .item > i {
        font-size: 2rem;
    }
    .avatar-size {
        width: 11rem;
        height: 11rem;
        top: -10rem !important;
    }
    .org-avatar-size {
        background-color: transparent !important;
        border: 0 !important;
        border-radius: 2px;
        width: 2rem;
        height: 2rem;
    }
    .github-orgs {
        display: inline-block;
        position: relative;
        top: -6rem;
        left: 13.7rem;
    }
    @media (min-width: 375px) {
        .github-orgs {
            top: -4.5rem;
            left: 17rem;
        }
    }
    @media (min-width: 425px) {
        .github-orgs {
            top: -4.5rem;
            left: 20.2rem;
        }
    }
    @media (min-width: 768px) {
        .github-orgs {
            top: -2.5rem;
            left: 17.2rem;
        }
    }
    @media (min-width: 1024px) {
        .github-orgs {
            top: 2.5rem;
            left: 23.2rem;;
        }
        .avatar-size {
            width: 15rem;
            height: 15rem;
        }
        .avatar > .item > i {
            font-size: 3rem;
        }
        .org-avatar-size {
            width: 3rem;
            height: 3rem;
        }
    }
</style>

