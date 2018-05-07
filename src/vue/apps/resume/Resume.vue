<template>
    <div class="container">
        <Navbar></Navbar>
        <Jumbotron :navlinks="navlinks" :position="resume.profile.position"></Jumbotron>
        <Content :resume="resume"></Content>
    </div>
</template>

<script>
    import Navbar from './components/Navbar.vue'
    import Jumbotron from './components/Jumbotron.vue'
    import Content from './components/Content.vue'

    export default {
        components: {
            Navbar,
            Jumbotron,
            Content
        },
        data: function() {
            return {
                navlinks: [
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
                    profile: {
                        title:'Sumary',
                        position:'Biomedical, Electrical and Software Engineer',
                        sumary:'Here I will dive into the task of writing a sumary for my professional profile. This will be hard. but i can do it! Here I will dive into the task of writing a sumary for my professional profile. This will be hard. but i can do it! Here I will dive into the task of writing a sumary for my professional profile. This will be hard. but i can do it! Here I will dive into the task of writing a sumary for my professional profile. This will be hard. but i can do it!',
                        picture:''
                    },
                    academics: {
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
                        ],
                    },
                    experiences: {
                        title:'Professional Experience',
                        experiences: [
                            {
                                'year':{
                                    'start':'2017',
                                    'end':'Present'
                                },
                                'position':'Research Engineer',
                                'institution': {
                                    'name':'Labratory of Technological Innoation in Health',
                                },
                                'description':'Responsible for the development of applications and systems for acquire, archive and emit medical exams reports remotely to the Brazilian Health Ministry through the Telehealth Brazil Network Program',
                                'references': [
                                    {
                                        'position':'Executive Director',
                                        'level':'PhD',
                                        'name':'Ricardo A. de Medeiros Valentim',
                                        'email':'ricardovalentim@ufrn.edu.br',
                                        'phone':'+55 (84) 991-116-55'
                                    },
                                    {
                                        'position':'Project Manager',
                                        'level':'MSc',
                                        'name':'Marcel da Câmara Riberito Dantas',
                                        'email':'mribeirodantas@ufrn.edu.br',
                                        'phone':'+55 (84) 981-094-570'
                                    }
                                ]
                            },
                            {
                                'year':{
                                    'start':'2017',
                                    'end':'2017'
                                },
                                'position':'Project Manager and TI Team Coordinator',
                                'institution': {
                                    'name':'Telxius Telecom S/A. through Oltec Group Ltd.',
                                },
                                'description':'Responsible for the coordination of the development team of the mobile applications Android and iOS as the Web/API systems for access control to the towers (internally named as sites) for the wireless communications service provider Vivo S/A and its service providers. The system had the purpose of making viable the access control via Bluetooth BLE padlock to the service team manager at their smartphone',
                                'references': [
                                    {
                                        'position':'Chief Compliance Officer',
                                        'level':'CCO',
                                        'name':'Victor Hugo de Paula Queiroz',
                                        'email':'victorhugopq@gmail.com',
                                        'phone':'+55 (62) 982-942-315'
                                    }
                                ]
                            }
                        ],
                    },
                    productions: {
                        title:'Scientific Production',
                        productions: [
                            {
                                'year':'2018',
                                'name':'Tele-Diagnostic Platform',
                                'type':'Software Registry',
                                'institution': {
                                    'name':'Brazilian Ministry of Health',
                                },
                                'description':'Through the implementation proposals for a remote medical report emission system, by the administrative rule nº 2.564/2011, which redefines the National Telehealth Network Program, a Web Service was developed to allow physicians from different regions inside the country located in great rates of professionals per inhabitant remotely emit medical reports for public health system users (patients) locate in regions where these same professionals have low rates per inhabitants',
                            }
                        ]
                    },
                    knowledges: {
                        title:'Technical Knowledge',
                        knowledges: [
                            {
                                'name':'AutoCAD-2D',
                                'company':'Autodesk',
                                'icon':'',
                                'versions': [
                                    '2008',
                                    '2010',
                                    '2015',
                                    '2016',
                                    '2017',
                                ]
                            },
                            {
                                'name':'AutoCAD-3D',
                                'company':'Autodesk',
                                'icon':'',
                                'versions': [
                                    '2016',
                                    '2017',
                                ]
                            }
                        ]
                    }
                }
            }
        }
    }
</script>

<style>
    .resume {
        padding: 1rem 1rem;
        margin-bottom: 2rem;
    }
    @media only screen and (max-width: 768px) and (min-width: 576px) {
        .presume {
            padding: 4rem 2rem;
        }
    }
    .resume-title {
        color: var(--primary-color);
    }
    @media only screen and (min-width: 768px) {
        .resume-title {
            margin-top: 0rem;
        }
    }
</style>