<template>
    <div id="app-resume">

        <div class="container">

            <header class="blog-header py-3">
                <div class="row flex-nowrap justify-content-between align-items-center">
                    <div class="col-4 pt-1">
                        <a class="text-muted" href="#">Subscribe</a>
                    </div>
                    <div class="col-4 text-center">
                        <a class="blog-header-logo text-dark" href="#">Large</a>
                    </div>
                    <div class="col-4 d-flex justify-content-end align-items-center">
                        <a class="btn btn-sm btn-outline-secondary" href="#">Sign up</a>
                    </div>
                </div>
            </header>

            <div class="nav-scroller py-1 mb-2 d-none d-md-block">
                <nav class="nav d-flex justify-content-between">
                    <a class="p-2 text-muted" href="#">World</a>
                    <a class="p-2 text-muted" href="#">U.S.</a>
                    <a class="p-2 text-muted" href="#">Technology</a>
                    <a class="p-2 text-muted" href="#">Design</a>
                    <a class="p-2 text-muted" href="#">Culture</a>
                    <a class="p-2 text-muted" href="#">Business</a>
                    <a class="p-2 text-muted" href="#">Politics</a>
                    <a class="p-2 text-muted" href="#">Opinion</a>
                    <a class="p-2 text-muted" href="#">Science</a>
                    <a class="p-2 text-muted" href="#">Health</a>
                    <a class="p-2 text-muted" href="#">Style</a>
                    <a class="p-2 text-muted" href="#">Travel</a>
                </nav>
            </div>

            <div class="jumbotron p-3 p-md-5 text-white rounded bg-dark">
                <div class="col-md-6 px-0">
                <h1 class="display-4 font-italic">Title of a longer featured blog post</h1>
                <p class="lead my-3">Multiple lines of text that form the lede, informing new readers quickly and efficiently about what's most interesting in this post's contents.</p>
                <p class="lead mb-0"><a href="#" class="text-white font-weight-bold">Continue reading...</a></p>
                </div>
            </div>

            <div class="row mb-2">
                <div class="col-md-6">
                <div class="card flex-md-row mb-4 box-shadow h-md-250">
                    <div class="card-body d-flex flex-column align-items-start">
                    <strong class="d-inline-block mb-2 text-primary">World</strong>
                    <h3 class="mb-0">
                        <a class="text-dark" href="#">Featured post</a>
                    </h3>
                    <div class="mb-1 text-muted">Nov 12</div>
                    <p class="card-text mb-auto">This is a wider card with supporting text below as a natural lead-in to additional content.</p>
                    <a href="#">Continue reading</a>
                    </div>
                    <img class="card-img-right flex-auto d-none d-md-block" data-src="holder.js/200x250?theme=thumb" alt="Card image cap">
                </div>
                </div>
                <div class="col-md-6">
                <div class="card flex-md-row mb-4 box-shadow h-md-250">
                    <div class="card-body d-flex flex-column align-items-start">
                    <strong class="d-inline-block mb-2 text-success">Design</strong>
                    <h3 class="mb-0">
                        <a class="text-dark" href="#">Post title</a>
                    </h3>
                    <div class="mb-1 text-muted">Nov 11</div>
                    <p class="card-text mb-auto">This is a wider card with supporting text below as a natural lead-in to additional content.</p>
                    <a href="#">Continue reading</a>
                    </div>
                    <img class="card-img-right flex-auto d-none d-md-block" data-src="holder.js/200x250?theme=thumb" alt="Card image cap">
                </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    export default {
        data: function() {
            return {
                selectedMainComponent: 'Blank',
                profile: {
                    name: {
                        first:'Natanael',
                        middle:'',
                        last:'de Freitas Neto'
                    }
                },
                langs: {
                    available: [
                        {
                            tag:'en-US',
                            en_description:'English',
                            own_description:'English',
                            en_country:'United States',
                            own_country:'United States',
                        }
                    ],
                    setted: 'en-US',
                },
                links: [
                    {
                        'string':'@natanaelfneto',
                        'destiny':'https://...',
                        'icon':''
                    },
                    {
                        'string':'Resumé',
                        'destiny':'https://...',
                        'icon':''
                    },
                    {
                        'string':'Github',
                        'destiny':'https://github.com/natanaelfneto',
                        'icon':''
                    },
                    {
                        'string':'LinkedIn',
                        'destiny':'https://...',
                        'icon':''
                    },
                    {
                        'string':'NEED Technology',
                        'destiny':'https://...',
                        'icon':''
                    }
                ],
                // resume: {
                //     profile: {
                //         title:'Sumary',
                //         position:'Biomedical, Electrical and Software Engineer',
                //         sumary:'Here I will dive into the task of writing a sumary for my professional profile. This will be hard. but i can do it! Here I will dive into the task of writing a sumary for my professional profile. This will be hard. but i can do it! Here I will dive into the task of writing a sumary for my professional profile. This will be hard. but i can do it! Here I will dive into the task of writing a sumary for my professional profile. This will be hard. but i can do it!',
                //         picture:''
                //     },
                //     academics: {
                //         title:'Academic Formation',
                //         degrees: [
                //             {
                //                 'year':'2018',
                //                 'level':'MSc',
                //                 'name':'Science, Technology and Innovation',
                //                 'department':'Science and Technology Department',
                //                 'school': {
                //                     'name':'Federal University of Rio Grande do Norte',
                //                     'acronym':'UFRN'
                //                 }
                //             },
                //             {
                //                 'year':'2016',
                //                 'level':'MBA',
                //                 'name':'Health Informatics',
                //                 'department':'Biomedical Engineering Department',
                //                 'school': {
                //                     'name':'Federal University of Rio Grande do Norte',
                //                     'acronym':'UFRN'
                //                 }
                //             },
                //             {
                //                 'year':'2015',
                //                 'level':'BEng',
                //                 'name':'Electrical Engineering',
                //                 'department':'Electric, Mecanic and Computer Engineering School',
                //                 'school': {
                //                     'name':'Federal University of Goiás',
                //                     'acronym':'UFG'
                //                 }
                //             }
                //         ],
                //     },
                //     experiences: {
                //         title:'Professional Experience',
                //         experiences: [
                //             {
                //                 'year':{
                //                     'start':'2017',
                //                     'end':'Present'
                //                 },
                //                 'position':'Research Engineer',
                //                 'institution': {
                //                     'name':'Labratory of Technological Innoation in Health',
                //                 },
                //                 'description':'Responsible for the development of applications and systems for acquire, archive and emit medical exams reports remotely to the Brazilian Health Ministry through the Telehealth Brazil Network Program',
                //                 'references': [
                //                     {
                //                         'position':'Executive Director',
                //                         'level':'PhD',
                //                         'name':'Ricardo A. de Medeiros Valentim',
                //                         'email':'ricardovalentim@ufrn.edu.br',
                //                         'phone':'+55 (84) 991-116-55'
                //                     },
                //                     {
                //                         'position':'Project Manager',
                //                         'level':'MSc',
                //                         'name':'Marcel da Câmara Riberito Dantas',
                //                         'email':'mribeirodantas@ufrn.edu.br',
                //                         'phone':'+55 (84) 981-094-570'
                //                     }
                //                 ]
                //             },
                //             {
                //                 'year':{
                //                     'start':'2017',
                //                     'end':'2017'
                //                 },
                //                 'position':'Project Manager and TI Team Coordinator',
                //                 'institution': {
                //                     'name':'Telxius Telecom S/A. through Oltec Group Ltd.',
                //                 },
                //                 'description':'Responsible for the coordination of the development team of the mobile applications Android and iOS as the Web/API systems for access control to the towers (internally named as sites) for the wireless communications service provider Vivo S/A and its service providers. The system had the purpose of making viable the access control via Bluetooth BLE padlock to the service team manager at their smartphone',
                //                 'references': [
                //                     {
                //                         'position':'Chief Compliance Officer',
                //                         'level':'CCO',
                //                         'name':'Victor Hugo de Paula Queiroz',
                //                         'email':'victorhugopq@gmail.com',
                //                         'phone':'+55 (62) 982-942-315'
                //                     }
                //                 ]
                //             }
                //         ],
                //     },
                //     productions: {
                //         title:'Scientific Production',
                //         productions: [
                //             {
                //                 'year':'2018',
                //                 'name':'Tele-Diagnostic Platform',
                //                 'type':'Software Registry',
                //                 'institution': {
                //                     'name':'Brazilian Ministry of Health',
                //                 },
                //                 'description':'Through the implementation proposals for a remote medical report emission system, by the administrative rule nº 2.564/2011, which redefines the National Telehealth Network Program, a Web Service was developed to allow physicians from different regions inside the country located in great rates of professionals per inhabitant remotely emit medical reports for public health system users (patients) locate in regions where these same professionals have low rates per inhabitants',
                //             }
                //         ]
                //     },
                //     knowledges: {
                //         title:'Technical Knowledge',
                //         knowledges: [
                //             {
                //                 'name':'AutoCAD-2D',
                //                 'company':'Autodesk',
                //                 'icon':'',
                //                 'versions': [
                //                     '2008',
                //                     '2010',
                //                     '2015',
                //                     '2016',
                //                     '2017',
                //                 ]
                //             },
                //             {
                //                 'name':'AutoCAD-3D',
                //                 'company':'Autodesk',
                //                 'icon':'',
                //                 'versions': [
                //                     '2016',
                //                     '2017',
                //                 ]
                //             }
                //         ]
                //     }
                // }
            }
        }
    }
</script>

<style scoped>
    /* stylelint-disable selector-list-comma-newline-after */

    .blog-header {
    line-height: 1;
    border-bottom: 1px solid #e5e5e5;
    }

    .blog-header-logo {
    font-family: "Playfair Display", Georgia, "Times New Roman", serif;
    font-size: 2.25rem;
    }

    .blog-header-logo:hover {
    text-decoration: none;
    }

    h1, h2, h3, h4, h5, h6 {
    font-family: "Playfair Display", Georgia, "Times New Roman", serif;
    }

    .display-4 {
    font-size: 2.5rem;
    }
    @media (min-width: 768px) {
    .display-4 {
        font-size: 3rem;
    }
    }

    .nav-scroller {
    position: relative;
    z-index: 2;
    height: 2.75rem;
    overflow-y: hidden;
    }

    .nav-scroller .nav {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-wrap: nowrap;
    flex-wrap: nowrap;
    padding-bottom: 1rem;
    margin-top: -1px;
    overflow-x: auto;
    text-align: center;
    white-space: nowrap;
    -webkit-overflow-scrolling: touch;
    }

    .nav-scroller .nav-link {
    padding-top: .75rem;
    padding-bottom: .75rem;
    font-size: .875rem;
    }

    .card-img-right {
    height: 100%;
    border-radius: 0 3px 3px 0;
    }

    .flex-auto {
    -ms-flex: 0 0 auto;
    -webkit-box-flex: 0;
    flex: 0 0 auto;
    }

    .h-250 { height: 250px; }
    @media (min-width: 768px) {
    .h-md-250 { height: 250px; }
    }

    .border-top { border-top: 1px solid #e5e5e5; }
    .border-bottom { border-bottom: 1px solid #e5e5e5; }

    .box-shadow { box-shadow: 0 .25rem .75rem rgba(0, 0, 0, .05); }

    /*
    * Blog name and description
    */
    .blog-title {
    margin-bottom: 0;
    font-size: 2rem;
    font-weight: 400;
    }
    .blog-description {
    font-size: 1.1rem;
    color: #999;
    }

    @media (min-width: 40em) {
    .blog-title {
        font-size: 3.5rem;
    }
    }

    /* Pagination */
    .blog-pagination {
    margin-bottom: 4rem;
    }
    .blog-pagination > .btn {
    border-radius: 2rem;
    }

    /*
    * Blog posts
    */
    .blog-post {
    margin-bottom: 4rem;
    }
    .blog-post-title {
    margin-bottom: .25rem;
    font-size: 2.5rem;
    }
    .blog-post-meta {
    margin-bottom: 1.25rem;
    color: #999;
    }

    /*
    * Footer
    */
    .blog-footer {
    padding: 2.5rem 0;
    color: #999;
    text-align: center;
    background-color: #f9f9f9;
    border-top: .05rem solid #e5e5e5;
    }
    .blog-footer p:last-child {
    margin-bottom: 0;
    }
</style>