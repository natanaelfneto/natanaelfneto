<template>
    <div id="app-resume">

        <div class="container">

            <Navbar :data="data"></Navbar>
            <Jumbotron :data="data"></Jumbotron>
            <ResumeFieldset :data="data"></ResumeFieldset>
            
        </div>

    </div>
</template>

<script>
    import Navbar from './components/Navbar.vue'
    import Jumbotron from './components/Jumbotron.vue'
    import ResumeFieldset from './components/ResumeFieldset.vue'

    export default {
        components: {
            Navbar,
            Jumbotron,
            ResumeFieldset
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
                            string:'natanaelfneto',
                            destiny:'http://natanaelfneto.com/',
                            icon:{
                                type:'fontawesome',
                                class:{
                                    base:'fas',
                                    name:'fa-at',
                                    custom:'fac-width fac-color-white',
                                },
                            },
                        },
                        {
                            string:'Resumé',
                            destiny:'#',
                            icon:{
                                type:'fontawesome',
                                class:{
                                    base:'fas',
                                    name:'fa-graduation-cap',
                                    custom:'',
                                },
                            },
                        },
                        {
                            string:'Github',
                            destiny:'#',
                            icon:{
                                type:'fontawesome',
                                class:{
                                    base:'fab',
                                    name:'fa-github-alt',
                                    custom:'',
                                },
                            },
                        },
                        {
                            string:'LinkedIn',
                            destiny:'#',
                            icon:{
                                type:'fontawesome',
                                class:{
                                    base:'fab',
                                    name:'fa-linkedin',
                                    custom:'',
                                },
                            },
                        },
                        {
                            string:'NEED Technology',
                            destiny:'#',
                            icon:{
                                type:'fontawesome',
                                class:{
                                    base:'fas',
                                    name:'fa-code',
                                    custom:'fac-width fac-color-white',
                                },
                            },
                        },
                    ],
                    resume: {
                        sumary: {
                            isActive: true,
                            title:'Sumary',
                            position: {
                                major:'Biomedical, Electrical and Software Engineer',
                                minor:'UI/UX Enthusiast and a Cat Lover'
                            },
                            content:'Here I will dive into the task of writing a sumary for my professional profile. This will be hard. but i can do it!',
                        },
                        academics: {
                            isActive: true,
                            title:'Academic Formation',
                            degrees: [
                                {
                                    'year':'2018',
                                    'level':'MSc',
                                    'name':'Science, Technology and Innovation',
                                    'department':'Science and Technology Department',
                                    'school': {
                                        'name':'Federal University of Rio Grande do Norte',
                                        'acronym':'UFRN'
                                    }
                                },
                                {
                                    'year':'2016',
                                    'level':'MBA',
                                    'name':'Health Informatics',
                                    'department':'Biomedical Engineering Department',
                                    'school': {
                                        'name':'Federal University of Rio Grande do Norte',
                                        'acronym':'UFRN'
                                    }
                                },
                                {
                                    'year':'2015',
                                    'level':'BEng',
                                    'name':'Electrical Engineering',
                                    'department':'Electric, Mecanic and Computer Engineering School',
                                    'school': {
                                        'name':'Federal University of Goiás',
                                        'acronym':'UFG'
                                    }
                                }
                            ]
                        },

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
                    activeTab:'natanaelfneto',
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