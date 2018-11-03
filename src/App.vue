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
    @media print {
        .breadcrumbs-v1, .badge {
            -webkit-print-color-adjust: exact;
        }
        #cp-resume {
            transform: scale(1.05);
        }
        [class*="col-md"], [class*="col-sm"], [class*="col-xs"] {
            float: none;
        }
        img {
            display: block;
        }
        #cp-github, .btn, .nav-item {
            display: none;
        }
        .print-col-lg-3 {
            flex: 0 0 25% !important;
            max-width: 25% !important;
        }
        .print-mt-lg-4 {
            margin-top: 1.5rem !important;
        }
        .print-d-lg-block {
            display: block !important;
        }
        address {
            margin-top: 1.5rem !important;
        }
        a {
            text-decoration: none !important;
        }
        div, p, a {
            color: black;
        }
        li.ml-auto.print {
            margin-left: 1rem !important;
        }
        li.mr-auto.print {
            margin-right: 1rem !important;
        }
        .print-d-none {
            display: none;
        }
        .print-col-12 {
            width: 100% !important;
        }
        #ContentTab {
            display: none;
        }
        .news-v3 .news-v3-in {
            padding-bottom: 1rem !important;
            padding-top: 1rem !important;
        }
        .news-v3-in>p {
            margin-bottom: 0 !important;
        }
        .print-place {
            position: relative !important;
            left: -1rem !important;
            margin-top: 5px !important;
        }
        .print-place>div>span {
            font-weight: bold !important;
            color: gray !important;
        }
        .print-mb-md-0 {
            margin-bottom: 0 !important;
        }
        .print-my-0 {
            margin-top: 0 !important;
            margin-bottom: 0 !important;
        }
        .hr {
            margin-top: 0rem !important;
            display: block !important;
        }
        .news-v3-in>ul {
            margin-bottom: 0 !important;
        }
        .headline>h2 {
            font-weight: bold !important;
            color: black !important;
        }
        .footer {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }
    }
</style>










