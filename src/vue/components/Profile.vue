<template>
    <div class="col-md-10 m-auto profile pb-0">
        <div class="row text-center">
            <div class="col-md-4 mt-auto">
                <img class="profile-image" src="../assets/image/profile.png" width="80%"/>
            </div>
            <div class="col-md-7 text-left">
                <h1 class="text-justify profile-info">Personal Information</h1>
                <p>
                    Here I will dive into the task of writing a sumary for my professional profile.
                    This will be hard. but i can do it! Here I will dive into the task of writing
                    a sumary for my professional profile. This will be hard. but i can do it!
                    Here I will dive into the task of writing a sumary for my professional profile.
                    This will be hard. but i can do it! Here I will dive into the task of writing
                    a sumary for my professional profile. This will be hard. but i can do it!
                </p>
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
        .profile {
            padding: 4rem 2rem;
        }
    }
    .profile-info {
        margin-bottom: 3rem;
        margin-top: -2rem;
        color: var(--primary-color);
    }
    .profile-image {
        border-style: solid;
        border-radius: 10rem;
        border-width: 0.2rem;
        border-color: var(--primary-color);
    }
</style>