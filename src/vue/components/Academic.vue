<template>
    <div class="col-md-10 m-auto academic">
        <div class="row text-center">
            <div class="col-md-4 mt-auto mb-auto"></div>
            <div class="col-md-7 text-left">
                <h1 class="text-justify academic-info">Academic Formation</h1>
            </div>
        </div>
        <div class="row text-center mb-4">
            <div class="col-md-4 mt-auto mb-auto">
                <img class="academic-image" src="../assets/image/academic-1.png" width="50%"/>
            </div>
            <div class="col-md-7 text-left academic-content">
                <span class="academic-year">2018</span>
                <span class="academic-degree">MSc, Science, Technology and Innovation</span>
                <span class="academic-school">Science and Technology Department<span>
                <span class="academic-institution">Federal University of Rio Grande do Norte - UFRN</span>
            </div>
        </div>
        <div class="row text-center mb-4">
            <div class="col-md-4 mt-auto mb-auto">
                <img class="academic-image" src="../assets/image/academic-1.png" width="50%"/>
            </div>
            <div class="col-md-7 text-left academic-content">
                <span class="academic-year">2016</span>
                <span class="academic-degree">MBA, Health Informatics</span>
                <span class="academic-school">Biomedical Engineering Department<span>
                <span class="academic-institution">Federal University of Rio Grande do Norte - UFRN</span>
            </div>
        </div>
        <div class="row text-center mb-4">
            <div class="col-md-4 mt-auto mb-auto">
                <img class="academic-image" src="../assets/image/academic-2.png" width="50%"/>
            </div>
            <div class="col-md-7 text-left academic-content">
                <span class="academic-year">2015</span>
                <span class="academic-degree">BEng, Electrical Engineering</span>
                <span class="academic-school">Electric, Mecanic and Computer Engineering School<span>
                <span class="academic-institution">Federal University of Goiás - UFG</span>
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
        .academic {
            padding: 4rem 2rem;
        }
    }
    .academic-info {
        margin-bottom: 3rem;
        margin-top: -2rem;
        color: var(--primary-color);
    }
    .academic-content span {
        display: block
    }
    .academic-year {
        color: #818181;
        font-weight: 600;
    }
    .academic-degree {
        font-weight: bold;
    }
    .academic-institution {

    }
</style>