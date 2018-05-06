<template>
    <div class="container">
        <Navbar></Navbar>
        <Jumbotron></Jumbotron>
        <Profile></Profile>
        <Academic></Academic>
        <Experience></Experience>
    </div>
</template>

<script>
    import Navbar from './components/Navbar.vue'
    import Jumbotron from './components/Jumbotron.vue'
    import Profile from './components/Profile.vue'
    import Academic from './components/Academic.vue'
    import Experience from './components/Experience.vue'

    export default {
        components: {
            Navbar,
            Jumbotron,
            Profile,
            Academic,
            Experience
        }
    }
</script>