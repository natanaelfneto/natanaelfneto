<template>
    <router-view :data="data"></router-view>
</template>

<script>
    import axios from 'axios';
    import data from '../data.json';

    export default {
        name: 'natanaelfneto',
        data: function() {
            return data
        },
        methods: {
            getGithubData(login) {

                let url = 'https://api.github.com/users/'+login;
                axios.get(url)
                .then(res => { 
                    this.data.sidebar.github.object.user = res.data;
                });

                let repos = [];
                this.data.sidebar.github.object.featured_repos.forEach(function (repo) {
                    let repo_url = 'https://api.github.com/repos/'+login+'/'+repo.name;
                    axios.get(repo_url)
                    .then(res => { repos.push(res.data) })
                });
                this.data.sidebar.github.object.featured_repos = repos;

                let orgs_url = url+'/orgs';
                axios.get(orgs_url)
                .then(res => { 
                    let orgs = [];
                    res.data.forEach(function (org) { 
                        let org_url = 'https://api.github.com/orgs/'+org.login;
                        axios.get(org_url)
                        .then(res => {
                            orgs.push(res.data);
                        });
                    });
                    this.data.sidebar.github.object.orgs = orgs;
                });
            },
        },
        created: function() {
            this.getGithubData(this.data.sidebar.github.object.user.login);
        }
    }
</script>

<style>
    :root {
        /* fade blue */
        --first-color: #1795a1;

        /* fade orange */
        --second-color: #c99900;

        /* fade dark gray */
        --third-color: #272727;
    }
    /* 
    .fade-blue {
        color: var(--first-color) !important;
    }
    .fade-orange {
        color: var(--second-color);
    }
    .fade-dark-gray {
        color: var(--third-color);
    }
    .bg-fade-blue {
        background-color: var(--first-color) !important;
    }
    .bg-fade-orange {
        background-color: var(--second-color);
    }
    .bg-fade-dark-gray {
        background-color: var(--third-color);
    }
    */
    a {
        color: var(--first-color);
    }
    a:hover {
        color: var(--second-color);
    }
    .headline h2,
    .headline h3,
    .headline h4 {
	    border-bottom: 2px solid var(--second-color);
    }
    .oldsh {
        font-family: 'Old Style';
    }
</style>










