<template>
    <div class="col-md-10 m-auto experience pb-0">
        <div class="row text-center">
            <div class="col-md-4 mt-auto mb-auto"></div>
            <div class="col-md-7 text-left">
                <h1 class="text-justify experience-info">Professional Experiences</h1>
            </div>
        </div>
        <div class="row text-center mb-4" v-for="experience in experiences">
            <div class="col-md-4 mt-auto mb-auto">
                <img class="experience-image" src="../assets/image/experience-1.png" width="50%"/>
            </div>
            <div class="col-md-7 text-left">
                <div class="experience-content">
                    <span class="experience-year">{{ experience.year.start }}-{{ experience.year.end }}</span>
                    <span class="experience-position">{{ experience.position }}</span>
                    <span class="experience-institution">{{ experience.institution.name }} - {{ experience.institution.acronym }}<span>
                    <span class="experience-description font-italic font-weight-light">
                        <p>
                            {{ experience.description }}
                        </p>
                    </span>
                </div>
                <div class="row mb-2" v-for="reference in experience.references">
                    <div class="col-md-3 text-secondary pr-0">
                        Reference:
                    </div>
                    <div class="col-md-9 font-weight-normal pl-0 experience-reference">
                        <div class="text-nowrap">
                            (<span class="reference-position font-italic">{{ reference.position }}</span>)
                            <span class="reference-name">{{ reference.level }} {{ reference.name }}</span>
                        </div>
                        <div class="text-nowrap">
                            <span class="reference-email">{{ reference.email }}</span>
                            /
                            <span class="reference-phone">{{ reference.phone }}</span>
                        </div>
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
                experiences: [
                    {
                        'year':{
                            'start':'2017',
                            'end':'Present'
                        },
                        'position':'Research Engineer',
                        'institution': {
                            'name':'Labratory of Technological Innoation in Health',
                            'acronym':'LAIS'
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
                            'acronym':''
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
                ]
            }
        }
    }
</script>

<style scoped>
    .profile {
        padding: 2rem 1rem;
        margin-bottom: 2rem;
    }
    @media (min-width: 576px) {
        .experience {
            padding: 4rem 2rem;
        }
    }
    .experience-info {
        margin-bottom: 3rem;
        margin-top: -2rem;
        color: var(--primary-color);
    }
    .experience-content span {
        display: block
    }
    .experience-year {
        color: #818181;
        font-weight: 600;
    }
    .experience-position {
        font-weight: bold;
    }
    .experience-institution {
        font-weight: 500;
    }
</style>