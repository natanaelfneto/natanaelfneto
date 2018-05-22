<template>
    <div id="app-resume">

        <div class="container">

            <Navbar :data="data"></Navbar>

            <Jumbotron :data="data"></Jumbotron>

            <!-- <div class="jumbotron p-3 p-md-5 text-white rounded bg-dark">
                <div class="col-md-6 px-0">
                <h1 class="display-4 font-italic">Title of a longer featured post</h1>
                <p class="lead my-3">Multiple lines of text that form the lede, informing new readers quickly and efficiently about what's most interesting in this post's contents.</p>
                <p class="lead mb-0"><a href="#" class="text-white font-weight-bold">Continue reading...</a></p>
                </div>
            </div> -->

            <!-- <div class="row mb-2">
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
            </div> -->

        </div>

    </div>
</template>

<script>
    import Navbar from './components/Navbar.vue'
    import Jumbotron from './components/Jumbotron.vue'

    export default {
        components: {
            Navbar,
            Jumbotron
        },
        data: function() {
            return {
                data: {
                    profile: {
                        name: {
                            full_name: {
                                first:'Natanael',
                                middle:'',
                                last:'de Freitas Neto'
                            },
                            display_name: 'Natanael F. Neto'
                        }
                    },
                    languages: {
                        available: [
                            {
                                language_tag:'en',
                                country_tag:'gb',
                                en_description:'English',
                                en_country:'Great Britain',
                                own_description:'English',
                                own_country:'Great Britain'
                            }
                        ],
                        setted: 'en-gb',
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
                    resume: {
                        'nada':'nada'
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
                    },
                    pusheenStatus:'dancing',
                    pusheenRememberMe: false,
                },
            }
        }
    }
</script>

<style scoped>
    
    h1, h2, h3, h4, h5, h6 {
        font-family: "Playfair Display", Georgia, "Times New Roman", serif;
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

    @media (min-width: 768px) {
        .h-md-250 { 
            height: 250px; 
        }
    }

    .box-shadow { 
        box-shadow: 0 .25rem .75rem rgba(0, 0, 0, .05);
    }

</style>