<template>
    <div class="col-md-10 m-auto experience">
        <div class="row text-center">
            <div class="col-md-4 mt-auto mb-auto"></div>
            <div class="col-md-7 text-left">
                <h1 class="text-justify experience-info">Professional Experiences</h1>
            </div>
        </div>
        <div class="row text-center mb-4">
            <div class="col-md-4 mt-auto mb-auto">
                <img class="experience-image" src="../assets/image/experience-1.png" width="50%"/>
            </div>
            <div class="col-md-7 text-left experience-content">
                <span class="experience-year">2017-Present</span>
                <span class="experience-position">Research Engineering</span>
                <span class="experience-institution">Labratory of Technological Innoation in Health - LAIS<span>
                <span class="experience-description font-italic font-weight-light">
                    <p class="mb-0">
                        Responsável por desenvolver aplicações e sistemas para aquisição, 
                        arquivamento e emissão de exames e laudos médicos remotos para o 
                        Ministério da Saúde (MS) do Brasil através do programa Telessaúde Brasil Redes.
                    </p>
                </span>
                <div class="col-md-3 font-weight-bold">
                    Reference:
                </div>
                <div class="col-md-9 font-weight-normal">
                    PhD. Ricardo A. de Medeiros Valentim +55 (84) 991-116-551
                </div>
            </div>
        </div>
        <div class="row text-center mb-4">
            <div class="col-md-4 mt-auto mb-auto">
                <img class="experience-image" src="../assets/image/experience-1.png" width="50%"/>
            </div>
            <div class="col-md-7 text-left experience-content">
                <span class="experience-year">2017-Present</span>
                <span class="experience-position">Research Engineering</span>
                <span class="experience-institution">Labratory of Technological Innoation in Health - LAIS<span>
                <span class="experience-description"><p></p></span>
            </div>
        </div>
        <div class="row text-center mb-4">
            <div class="col-md-4 mt-auto mb-auto">
                <img class="experience-image" src="../assets/image/experience-1.png" width="50%"/>
            </div>
            <div class="col-md-7 text-left experience-content">
                <span class="experience-year">2017-Present</span>
                <span class="experience-position">Research Engineering</span>
                <span class="experience-institution">Labratory of Technological Innoation in Health - LAIS<span>
                <span class="experience-description"><p></p></span>
            </div>
        </div>
    </div>
</template>

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
    .experience-description {
        
    }
    .experience-reference {
        display: initial;
    }
    .experience-reference span {
        display: initial;
        margin-bottom: 0;
    }
    .experience-reference-contact {
        display: block !important;
    }
</style>