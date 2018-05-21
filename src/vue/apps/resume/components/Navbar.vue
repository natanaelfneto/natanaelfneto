<template>
    <div id="component-navbar">

        <header class="blog-header py-1 py-sm-3">
            <div class="flex-nowrap justify-content-between align-items-center d-none d-md-block">
                <div class="row">
                    <div class="col-md-4 col-sm-12 py-1 my-auto">

                        <a class="text-muted" href="#">Language:</a>
                        <span class="py-2 ml-auto">
                            <a class="text-muted mx-1" href="#">English</a>
                            <span aria-hidden="true" class="flag-icon flag-icon-gb"></span>
                        </span>

                    </div>
                    <div class="col-md-4 col-sm-12 py-1 text-center">
                        <a class="blog-header-logo text-nowrap text-dark" href="#">Natanael F. Neto</a>
                    </div>
                    <div class="col-md-4 col-sm-12 d-flex justify-content-end align-items-center">
                        <a class="btn btn-sm btn-outline-secondary" href="#">Sign in</a>
                    </div>
                </div>
            </div>
        </header>

        <nav class="navbar navbar-expand-md navbar-light rounded">

            <span class="blog-header-logo text-dark d-md-none d-lg-none d-xl-none">Natanael F. Neto</span>

            <div class="navbar-collapse d-md-block collapse" id="navbarsExample10" style="display: ">
                <ul class="navbar-nav justify-content-md-between">

                    <li class="nav-item d-inline-flex d-md-none d-lg-none d-xl-none">
                        <a class="text-muted py-2" href="#">Language:</a>
                        <span class="py-2 ml-auto">
                            <a class="text-muted py-2 mx-1" href="#">English</a>
                            <span aria-hidden="true" class="flag-icon flag-icon-gb"></span>
                        </span>
                    </li>

                    <li class="row nav-item d-inline-flex">
                        <div class="py-2 text-muted item text-center">
                            <i aria-hidden="true" class="fas fa-at fac-width fac-color-white"></i>
                        </div>
                        <a class="py-2 text-muted" href="#">natanaelfneto</a>
                    </li>

                    <li class="row nav-item d-inline-flex">
                        <div class="py-2 text-muted item text-center">
                            <i aria-hidden="true" class="fas fa-graduation-cap"></i>
                        </div>
                        <a class="py-2 text-muted" href="#">Resumé</a>
                    </li>

                    <li class="row nav-item d-inline-flex">
                        <div class="py-2 text-muted item text-center">
                            <i aria-hidden="true" class="fab fa-github-alt"></i>
                        </div>
                        <a class="py-2 text-muted" href="#">Github</a>
                    </li>

                    <li class="row nav-item d-inline-flex">
                        <div class="py-2 text-muted item text-center">
                            <i aria-hidden="true" class="fab fa-linkedin"></i>
                        </div>
                        <a class="py-2 text-muted" href="#">LinkedIn</a>
                    </li>

                    <li class="row nav-item d-inline-flex">
                        <div class="py-2 text-muted item text-center">
                            <i aria-hidden="true" class="fas fa-code fac-width fac-color-white"></i>
                        </div>
                        <a class="py-2 text-muted" href="#">NEED Technology</a>
                    </li>

                    <li class="row nav-item dropdown d-md-none d-lg-none d-xl-none">

                        <div class="py-2 text-muted item text-center">
                            <i aria-hidden="true" class="fas fa-user-astronaut"></i>
                        </div>

                        <a 
                            class="py-2 text-muted" 
                            href="#" 
                            id="dropdownSignInForm" 
                            data-toggle="dropdown" 
                            aria-haspopup="true" 
                            aria-expanded="false">
                            Sign in
                        </a>

                        <div class="col-xs-12 col-sm-12 dropdown-menu bg-light text-secondary" aria-labelledby="dropdownSignInForm">
                            <form class="px-4 py-3">
                                <div class="form-group">
                                    <label for="dropdownFormEmail">Email address</label>
                                    <input 
                                        type="email" 
                                        class="form-control" 
                                        id="dropdownFormEmail"
                                        autocomplete="current-user-email"
                                        placeholder="email@example.com" />
                                </div>
                                <div class="form-group">
                                    <label for="dropdownFormPassword">Password</label>
                                    <input 
                                        type="password" 
                                        class="form-control" 
                                        id="dropdownFormPassword" 
                                        autocomplete="current-password"
                                        placeholder="Password" />
                                </div>
                                <div class="form-check mb-2">
                                    <input type="checkbox" class="form-check-input" id="dropdownCheck">
                                    <label class="form-check-label" for="dropdownCheck">Remember me</label>
                                </div>
                                <button type="button" class="btn btn-block btn-light">Sign in</button>
                            </form>
                            <div class="dropdown-divider"></div>
                            <a class="dropdown-item text-secondary" href="#">Forgot password?</a>
                        </div>

                    </li>

                </ul>
            </div>

            <button 
                class="navbar-toggler collapsed ml-auto" 
                type="button" 
                data-toggle="collapse" 
                data-target="#navbarsExample10" 
                aria-controls="navbarsExample10" 
                aria-expanded="false" 
                aria-label="Toggle navigation">
                <span class="item-box">
                    <span class="item">
                        <span aria-hidden="true" class="icon-cup"></span>
                    </span>
                </span>
            </button>
            
        </nav>

    </div>
</template>

<script>
</script>

<style scoped>

    .fac-width {
        -webkit-text-stroke-width: 0.02rem;
    }

    .fac-color-white {
        -webkit-text-stroke-color: white;
    }

    @media (min-width: 768px) {
        .navbar-expand-md .navbar-collapse {
            display: unset !important;
        }

        .blog-header {
            line-height: 1;
            border-bottom: 1px solid #e5e5e5;
        }

        .blog-header-logo {
            line-height: unset !important;
            font-family: "Playfair Display", Georgia, "Times New Roman", serif;
            font-size: 2.25rem;
        }

        .blog-header-logo:hover {
            text-decoration: none;
        }

    }

    .blog-header-logo {
        line-height: 2;
        font-family: "Playfair Display", Georgia, "Times New Roman", serif;
        font-size: 1.5rem;
    }

    button[aria-expanded=true] {
        width: 100%;
        border-radius: 0;
        border-top: 1px solid #e5e5e5;
        padding-bottom: 0px;
        padding-top: 0.75rem;
        margin-top: 0.75rem;
    }
    
    button[aria-expanded=true] span[class=item]{
        font-size: 2rem;
    }

    .navbar-toggler {
        border: 0;
    }

    button:focus {
        outline: none;
    }
    
    .nav-item>.item {
        min-width: 2rem;
    }

</style>