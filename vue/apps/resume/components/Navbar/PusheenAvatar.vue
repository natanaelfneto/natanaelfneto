<template>
    <div id="component-navbar-sign-in-form-pusheen-avatar">
        <div>
            <div id="pusheen" :class="data.pusheenStatus"></div>
            <div id="pusheen-remember-me" :class="{ 'remembering':data.pusheenRememberMe }"></div>
        </div>
        <div id="sign-in-avatar"></div>
    </div>
</template>

<script>
    export default {
        props: {
            data: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>
    #sign-in-avatar {
        background-color: #FCF0E4;
        z-index: -1;
        border-color: #5e5e5e;
        border-radius: 10rem;
        border: 1px solid;
        height: 12rem;
        width: 12rem;
        margin: auto;
        position: relative;
        top: 0rem;
        margin-top: -9rem;
    }
    #pusheen {
        background-size: contain;
        background-position: center center;
        background-repeat: no-repeat;
        min-height: 9rem;
        max-height: 9rem;
        margin-bottom: -1rem;
        margin-top: 0.5rem;

        position: relative;
        top: 2.5rem;
        left: 0.6rem;

        animation-play-state: running;
        animation-duration: 0.3s;
        animation-delay: 0s;
        animation-iteration-count: infinite;
        animation-direction: alternate;
        animation-timing-function: step-end;           
    }
    #pusheen-remember-me {
        display: none;
        background-size: contain;
        background-position: center center;
        background-repeat: no-repeat;
        min-height: 9rem;
        max-height: 9rem;
        position: relative;
        top: -5.5rem;
        left: 0.5rem;
        margin-bottom: -17rem;
        animation-play-state: running;
        animation-duration: 0.3s;
        animation-delay: 0s;
        animation-iteration-count: infinite;
        animation-direction: alternate;
        animation-timing-function: step-end;
    }
    .standing {
        background-image: url('../../../../assets/image/pusheen/standing.png');
    }
    .dancing {
        animation-name: pusheen-dancing;
    }
    .typing {
        animation-name: pusheen-typing;
    }
    .spying {
        animation-name: pusheen-spying;
    }
    .remembering {
        display: block !important;
        animation-name: pusheen-remembering;
    }
    @keyframes pusheen-dancing {
        0%  { background-image: url('../../../../assets/image/pusheen/dancing_step_1.png'); }
        33%  { background-image: url('../../../../assets/image/pusheen/dancing_step_2.png'); }
        66%  { background-image: url('../../../../assets/image/pusheen/dancing_step_3.png'); }
        100% { background-image: url('../../../../assets/image/pusheen/dancing_step_4.png'); }
    }
    @keyframes pusheen-typing {
        0%  { background-image: url('../../../../assets/image/pusheen/typing_step_1.png'); }
        33%  { background-image: url('../../../../assets/image/pusheen/typing_step_2.png'); }
        66%  { background-image: url('../../../../assets/image/pusheen/typing_step_3.png'); }
        100% { background-image: url('../../../../assets/image/pusheen/typing_step_4.png'); }
    }
    @keyframes pusheen-spying {
        0%  { background-image: url('../../../../assets/image/pusheen/spying_step_1.png'); }
        33%  { background-image: url('../../../../assets/image/pusheen/spying_step_2.png'); }
        66%  { background-image: url('../../../../assets/image/pusheen/spying_step_3.png'); }
        100% { background-image: url('../../../../assets/image/pusheen/spying_step_4.png'); }
    }
    @keyframes pusheen-remembering {
        0%  { background-image: url('../../../../assets/image/pusheen/remembering_step_1.png'); }
        33%  { background-image: url('../../../../assets/image/pusheen/remembering_step_2.png'); }
        66%  { background-image: url('../../../../assets/image/pusheen/remembering_step_3.png'); }
        100% { background-image: url('../../../../assets/image/pusheen/remembering_step_4.png'); }
    }
</style>