<template>
    <div id="component-resume-fieldset-academic-formation">        
            <div v-for="(degree, index, i) in data.resume.academics.degrees" class="row py-2 ml-0 academic-card">
                <div class="profile w-100">
                    <div class="photo shadow">
                        <img src="../../assets/image/logos/ufg.png">
                    </div>
                    <div class="content mt-2 ml-5 pl-3">
                        <div class="row w-100 px-3">
                            <span>{{ degree.level }}</span>
                            <span class="mx-2">in</span>
                            <span>{{ degree.name }}</span>
                            <span class="ml-auto">{{ degree.year }}<span>
                        </div>
                        <div class="row w-100 px-3">
                            <span>{{ degree.department }}</span>
                        </div>
                        <div class="row w-100 px-3">
                            <span>{{ degree.school.name }}</span>
                            <span class="mx-2">-</span>
                            <span>{{ degree.school.acronym }}</span>
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
    .profile {
        margin-left: 50px;
        height: 100px;
        background-color: #fafafa;
        box-shadow: 0 0 1rem #babbbc;
    }
    .profile .photo {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        overflow: hidden;
        border: 2px solid #0075be;
        background-color: #fafafa;
        margin-left: -50px;
    }
    .profile .photo img {
        width: 100%;
        position: relative;
        top: 1rem;
    }
    .content {
        position: relative;
        top: -6rem;
    }
</style>