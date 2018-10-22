<template>
    <router-view :data="data"></router-view>
</template>

<script>
    export default {
        name: 'natanaelfneto',
        data: function() {
            return {
                data: {
                    background_image: 'assets/img/bg-gyn.png',
                    profile_image: 'assets/img/profile.png'
                },
            }
        },
    }
</script>











