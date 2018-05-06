<template>
    <div class="col-md-10 m-auto academic pb-0">
        <div class="row text-center">
            <div class="col-md-4 mt-auto mb-auto"></div>
            <div class="col-md-7 text-left">
                <h1 class="text-justify academic-info">Academic Formation</h1>
            </div>
        </div>
        <div class="row text-center mb-4" v-for="degree in degrees">
            <div class="col-md-4 mt-auto mb-auto">
                <img class="academic-image" src="../assets/image/academic-1.png" width="50%"/>
            </div>
            <div class="col-md-7 text-left academic-content">
                <span class="academic-year">{{ degree.year }}</span>
                <span class="academic-degree">
                    {{ degree.level }} <span class="font-weight-normal font-italic">in</span> {{ degree.name }}
                </span>
                <div>{{ degree.department }}<div>
                <div>{{ degree.school.name }} - {{ degree.school.acronym }}</div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data: function() {
            return {
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
        .academic {
            padding: 4rem 2rem;
        }
    }
    .academic-info {
        margin-bottom: 3rem;
        margin-top: -2rem;
        color: var(--primary-color);
    }
    .academic-year {
        color: #818181;
        font-weight: 600;
    }
    .academic-degree {
        font-weight: bold;
    }
</style>