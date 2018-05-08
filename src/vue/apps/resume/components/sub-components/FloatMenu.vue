<template>
    <div class="menu" :style="setPosition()">
        <div>FLOAT MENU Opt1</div>
        <div>FLOAT MENU Opt2</div>
        <div>FLOAT MENU Opt3</div>
        <div>FLOAT MENU Opt4</div>
    </div>
</template>

<script>
    export default {
        props: {
            floatMenu: {
                type: Object,
                required: true
            }
        },
        methods: {
            setPosition() {
                return { 
                    left: this.floatMenu.xyPosition.x + 'px',
                    top: this.floatMenu.xyPosition.y + 'px',
                    width: this.floatMenu.xySize.width + 'px',
                    height: this.floatMenu.xySize.height + 'px'
                }
            }
        }
    }
</script>

<style scoped>
    .menu {
        position: fixed;
        z-index: 100;
        background-color: black;
        color: white;
    }
</style>