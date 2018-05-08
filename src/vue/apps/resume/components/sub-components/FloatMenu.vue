<template>
    <div class="menu" :style="setPosition(floatMenu)">
        <div v-for="option in floatMenu.options">
            <span>{{ option }}</span>
        </div>
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
            setPosition(floatMenu) {
                var floatParams = this.floatMenu.floatParams
                var sourceParams = this.floatMenu.sourceParams
                if(floatMenu.fixed){
                    var position = { 
                        left: sourceParams.x + 'px',
                        top: 30 + sourceParams.y + 'px',
                        width: floatParams.width + 'px',
                        height: floatParams.height + 'px'
                    }
                } else {
                    var position = { 
                        left: floatParams.x + 'px',
                        top: floatParams.y + 'px',
                        width: floatParams.width + 'px',
                        height: floatParams.height + 'px'
                    }
                }
                return position;
            }
        }
    }
</script>

<style scoped>
    .menu {
        position: fixed;
        z-index: 100;
        background-color: #fafafa;
        color: #4f6984;
        box-shadow: 3px 3px #536472;
        border: 1px solid #4f6994;
    }
    .menu div {
        min-height: 2rem;
    }
    .menu div:hover {
        background-color: #b2c5d8;
        cursor: pointer;
    }
    .menu span {
        margin: 1rem;
        vertical-align: middle;
    }
</style>