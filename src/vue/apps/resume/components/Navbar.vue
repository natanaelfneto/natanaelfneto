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

                    <li class="nav-item d-inline-flex">
                        <div class="nav-link item">
                            <span aria-hidden="true" class="icon-eyeglasses"></span>
                        </div>
                        <a class="nav-link text-muted" href="#">@natanaelfneto</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link text-muted" href="#">Resumé</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link text-muted" href="#">Github</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link text-muted" href="#">LinkedIn</a>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link text-muted" href="#">NEED Tecnology</a>
                    </li>

                    <li class="nav-item dropdown d-md-none d-lg-none d-xl-none">

                        <a 
                            class="nav-link text-muted dropdown-toggle" 
                            href="https://example.com" 
                            id="dropdown10" 
                            data-toggle="dropdown" 
                            aria-haspopup="true" 
                            aria-expanded="false">
                            Dropdown
                        </a>

                        <div class="dropdown-menu" aria-labelledby="dropdown10">
                            <a class="dropdown-item" href="#">Action</a>
                            <a class="dropdown-item" href="#">Another action</a>
                            <a class="dropdown-item" href="#">Something else here</a>
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

<style>

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
    

</style>