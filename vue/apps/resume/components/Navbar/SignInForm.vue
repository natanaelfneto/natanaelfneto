<template>
    <div 
        id="component-navbar-sign-in-form" 
        class="col-xs-12 col-sm-12 dropdown-menu dropdown-menu-right bg-light text-secondary" 
        aria-labelledby="dropdownSignInForm">
        <PusheenAvatar :data="data"></PusheenAvatar>
        <form class="px-4 py-3">
            <div class="form-group">
                <label>Email address</label>
                <input 
                    type="email" 
                    class="form-control" 
                    autocomplete="current-user-email"
                    placeholder="email@example.com" 
                    @click="data.pusheenStatus='typing'" />
            </div>
            <div class="form-group">
                <label>Password</label>
                <input 
                    type="password" 
                    class="form-control" 
                    autocomplete="current-password"
                    placeholder="Password" 
                    @click="data.pusheenStatus='spying'" />
            </div>
            <div class="form-check mb-2">
                <input 
                    type="checkbox" 
                    class="form-check-input"
                    @click="pusheenRememberToggler($event)" />
                <label class="form-check-label">Remember me</label>
            </div>
            <input type="button" class="btn btn-block btn-secondary" value="Sign in" @click="SignInEvent()" />
        </form>
        <div class="dropdown-divider"></div>
        <a class="dropdown-item text-secondary" href="#">Forgot password?</a>
    </div>
</template>

<script>
    import PusheenAvatar from './PusheenAvatar.vue'

    export default {
        components: {
            PusheenAvatar
        },
        props: {
            data: {
                type: Object,
                required: true
            }
        },
        methods: {
            SignInEvent() {
                console.log('signing in...')
            },
            pusheenRememberToggler(e) {
                this.data.pusheenRememberMe = e.target.checked;
            }
        }
    }
</script>

<style scoped>
    #component-navbar-sign-in-form {
        min-width: 18rem;
    }
</style>