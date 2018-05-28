<template>
    <div id="component-resume-fieldset-academic-formation">        
        <div 
            v-for="(degree, index, i) in data.resume.academics.degrees"
            class="row py-2 mx-0 academic-card">
            <div class="col-sm-12 col-md-3 image-content">
                <div class="d-flex">
                    <img class="mx-auto" :src="require('../../assets/image/schools/'+degree.department.acronym+'.png')"/>
                </div>
            </div>

            <div 
                class="col-sm-12 col-md-9 detail-content">
                <div class="row"><kbd class="font-weight-bold">{{ degree.level }}</kbd></div>
                <div class="coll">
                    <div class="ml-auto font-weight-bold text-muted content-year">{{ degree.year }}</div>
                    <div class="font-weight-500 content-row">{{ degree.title.name }}</div>    
                    <div class="content-row">{{ degree.department.name }}</div>
                    <div class="content-row">
                        <span>{{ degree.school.name }}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            data: {
                type: Object,
                required: true
            }
        },
    }
</script>

<style scoped>
    .academic-card {
        width: 100%;
        margin-bottom: -2rem;
    }
    .academic-card > .image-content {
        height: 100px;
    }
    .academic-card > .image-content > div {
        height: 100px; 
        width: 100%;
    }
    .academic-card > .image-content > div > img{
        width: 100px;
        border-radius: 50%;
        border: 1px solid #ced4da;
        z-index: 1;
    }
    .academic-card > .detail-content {
        position: relative;
        top: -3rem;
        left: unset;
        background-color: #fff;
        height: 100%;
        box-shadow: 0.01rem 0.1rem 0.1rem 0 #818182b8;
        padding-left: 15px;
        padding-top: 40px;
    }
    .academic-card > .detail-content > div > kbd {
        z-index: 1;
        margin-left: auto;
        margin-right: auto;
        top: -6rem;
        position: relative;
        left: -2rem;
    }
    .academic-card > .detail-content > .coll > .content-year {
        display: table; 
        position: relative;
        top: -3.5rem;
    }
    .academic-card > .detail-content > .coll > .content-row,
    .academic-card > .detail-content > .coll > .content-row > span {
        white-space: unset !important;
    }
    .academic-card > .detail-content > .coll > div {
        position: relative; 
        top: -1.5rem;
    }
    .font-weight-500 {
        font-weight: 500;
    
    }
    @media (min-width: 375px) {
        .academic-card > .detail-content > .coll > .content-year {
            top: -3.5rem;
            left: unset;
        }
    }
    @media (min-width: 375px) {
        .academic-card > .detail-content {
            height: 155px;
        }
        .academic-card > .detail-content > .coll > .content-year {
            top: -3.5rem;
            left: unset;
        }
        .academic-card > .detail-content > .coll > .content-row {
            top: -2.5rem;
        }
    }
    @media (min-width:425px) {
        .academic-card > .detail-content {
            height: 100%;
        }
        .academic-card > .detail-content > .coll {
            margin-bottom: -10%;
        }
        .academic-card > .detail-content > .coll > .content-year {
            top: -3.5rem;
            left: unset;
        }
    }
    @media (min-width: 768px) {
        .academic-card {
            width: 115%;
            margin-bottom: unset;
        }
        .academic-card > .detail-content {
            top: unset;
            left: -13%;
            height: 100px;
            padding-left: 10%;
            padding-top: unset;
        }
        .academic-card > .detail-content > div > kbd {
            z-index: 1;
            margin-left: -3rem;
            margin-right: unset;
            top: 0.7rem;
            position: relative;
            left: 1em;
        }
        .academic-card > .detail-content > .coll > .content-year {
            top: -1rem;
            left: unset;
        }
        .academic-card > .detail-content > .coll > .content-row,
        .academic-card > .detail-content > .coll > .content-row > span {
            white-space: nowrap !important;
        }
    }
    /*.profile {
        margin-left: 50px;
        height: 97px;
        background-color: white;
        box-shadow: 0.01rem 0.05rem 0.1rem 0rem #818182b8;
        border-radius: 5px;
    }
    .profile .photo {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        overflow: hidden;
        border: 1px solid #ced4da;
        background-color: #e9ecef;
        margin-left: -50px;
    }
    .profile .photo img {
        width: 100%;
        position: relative;
    }
    .img-logo {
        height: 50px;
    }
    .img-logo img {
        width: 50px;
        margin-right: 2rem;
        position: relative;
        top: -5rem;
    }
    .content {
        position: relative;
        top: -10.7rem;
    }
    .font-weight-500 {
        font-weight: 500;
    }
    kbd {
        position: relative;
        left: -4rem;
        top: -6rem;
    }*/
</style>