<template>
    <router-view :data="data"></router-view>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'natanaelfneto',
        data: function() {
            return {
                data: {
                    activeTab: 'Resume',
                    github: {
                        username: 'natanaelfneto',
                        user: '',
                        orgs: '',
                        repos: [
                            {
                                name: 'pythontail',
                                data: '',
                            },
                            {
                                name: 'dicompopulate',
                                data: '',
                            },
                            {
                                name: 'codedir2pdf',
                                data: '',
                            },
                        ],
                    },
                    background_image: 'assets/img/bg-gyn.png',
                    profile_image: 'assets/img/profile.png',
                    lais_image: 'assets/img/lais.png',
                    academic: [
                        {
                            degree: 'Master',
                            title: 'Ciência, Tecnologia e Inovação',
                            acronym: 'MSc',
                            year: {
                                start: '',
                                end: '2018',
                            },
                            department: 'Departamento de Ciência e Tecnologia',
                            institution: 'Universidade Federal do Rio Grande do Norte',
                        },
                        {
                            degree: 'Specialist',
                            title: 'Informática em Saúde',
                            acronym: 'Esp',
                            year: {
                                start: '',
                                end: '2017',
                            },
                            department: 'Departamento de Engenharia Biomédica',
                            institution: 'Universidade Federal do Rio Grande do Norte',
                        },
                        {
                            degree: 'Bachelor',
                            title: 'Engenharia Elétrica',
                            acronym: 'BEng',
                            year: {
                                start: '',
                                end: '2015',
                            },
                            department: 'Escola de Engenharia Elétrica, Mecânica e de Computação',
                            institution: 'Universidade Federal de Goiás',
                        },
                    ],
                    experiences: [
                        {
                            description: 'Responsável por desenvolver aplicações e sistemas para aquisição, arquivamento e emissão de exames e laudos médicos remotos para o Ministério da Saúde (MS) do Brasil através do programa Telessaúde Brasil Redes',
                            place: {
                                name: 'Laboratório de Inovação Tecnológica em Saúde',
                                acronym: 'LAIS',
                                image: {
                                    logo: 'assets/img/lais.png',
                                    icon: 'assets/img/lais.png',
                                },
                                page_url: 'http://lais.huol.ufrn.br/',
                                parents: [
                                    {
                                        name: 'Programa Nacional Telessaúde Brasil Redes',
                                        acronym: 'TELESSAÚDE',
                                        image: {
                                            logo: 'assets/img/telessaude.png',
                                            icon: 'assets/img/telessaude.png',
                                        },
                                        page_url: 'http://dab.saude.gov.br/portaldab/ape_telessaude.php',
                                    },
                                    {
                                        name: 'Universidade Federal do Rio Grande do Norte',
                                        acronym: 'UFRN',
                                        image: {
                                            logo: 'assets/img/ufrn.png',
                                            icon: 'assets/img/ufrn.png',
                                        },
                                        page_url: 'https://www.ufrn.br/',
                                    },
                                    {
                                        name: 'Ministério da Saúde do Brasil',
                                        acronym: 'MS-BR',
                                        image: {
                                            logo: 'assets/img/msbr.png',
                                            icon: 'assets/img/msbr.png',
                                        },
                                        page_url: 'http://portalms.saude.gov.br/',
                                    },
                                ],
                            },
                            position: 'Engenheiro Pesquisador Sênior',
                            location: 'Natal, RN',
                            year: {
                                start: '2017',
                                end: '2018'
                            }
                        },
                        {
                            description: 'Responsável por coordenar a equipe de desenvolvimento das aplicações mobile Android e iOS junto com os sistemas Web/API de controle de acessos às torres (sites) da operadora Vivo S/A por empresas prestadoras de serviços. O sistema viabilizava acesso às torres (sites) por meio de cadeados Bluetooth BLE com o acompanhamento dos gestores das equipes das empresas prestadoras de serviços via aparelhos smartphone com conexão, ou não, à internet',
                            place: {
                                name: 'Need Tecnlogogia e Serviços',
                                acronym: 'NEED®',
                                image: {
                                    logo: 'assets/img/need.png',
                                    icon: 'assets/img/need.png',
                                },
                                page_url: '',
                                parents: [
                                    {
                                        name: 'Grupo Oltec Ltda',
                                        acronym: 'OLTEC',
                                        image: {
                                            logo: 'assets/img/oltec.png',
                                            icon: 'assets/img/oltec.png',
                                        },
                                        page_url: 'http://www.oltec.com.br/en/',
                                    },
                                    {
                                        name: 'Telxius Telecom S/A',
                                        acronym: 'TELXIUS',
                                        image: {
                                            logo: 'assets/img/telxius.png',
                                            icon: 'assets/img/telxius.png',
                                        },
                                        page_url: 'https://telxius.com/en/',
                                    },
                                ],
                            },
                            position: 'Coordenador da Equipe de Tecnologia da Informação',
                            location: 'Rio de Janeiro, RJ',
                            year: {
                                start: '2017',
                                end: '2017'
                            }
                        },
                        {
                            description: 'Responsável por desenvolver aplicações e sistemas para aquisição, arquivamento e acesso remoto de exames de imagens médicas de acordo com os padrões HL7 e DICOM para o Hospital Universitário Onofre Lopes, vinculado à rede da Empresa Brasileira de Serviços Hospitalares (EBSERH).',
                            place: {
                                name: 'Laboratório de Inovação Tecnológica em Saúde',
                                acronym: 'LAIS',
                                image: {
                                    logo: 'assets/img/lais.png',
                                    icon: 'assets/img/lais.png',
                                },
                                page_url: 'http://lais.huol.ufrn.br/',
                                parents: [
                                    {
                                        name: 'Hospital Universitário Onofre Lopes',
                                        acronym: 'HUOL',
                                        image: {
                                            logo: 'assets/img/huol.png',
                                            icon: 'assets/img/huol.png',
                                        },
                                        page_url: 'http://www.ebserh.gov.br/web/huol-ufrn',
                                    },
                                    {
                                        name: 'Empresa Brasileira de Serviços Hospitalares',
                                        acronym: 'EBSERH',
                                        image: {
                                            logo: 'assets/img/ebserh.png',
                                            icon: 'assets/img/ebserh.png',
                                        },
                                        page_url: 'http://www.ebserh.gov.br/',
                                    },
                                    {
                                        name: 'Universidade Federal do Rio Grande do Norte',
                                        acronym: 'UFRN',
                                        image: {
                                            logo: 'assets/img/ufrn.png',
                                            icon: 'assets/img/ufrn.png',
                                        },
                                        page_url: 'https://www.ufrn.br/',
                                    },
                                ],
                            },
                            position: 'Engenheiro Pesquisador',
                            location: 'Natal, RN',
                            year: {
                                start: '2016',
                                end: '2017'
                            }
                        },
                        {
                            description: 'Responsável pela coordenação do desenvolvimento e manutenção de hardware e software de aparelhos de imagens médicas e dos sistemas administrativos internos da empresa',
                            place: {
                                name: 'CTX Assistência e Revenda de Equipamentos de Imagens Médica Ltda',
                                acronym: 'CTX®',
                                image: {
                                    logo: 'assets/img/ctx.png',
                                    icon: 'assets/img/ctx.png',
                                },
                                page_url: '',
                                parents: [],
                            },
                            position: 'Engenheiro Biomédico e Eletrônico',
                            location: 'Goiânia, GO',
                            year: {
                                start: '2014',
                                end: '2016'
                            }
                        },
                        {
                            description: 'Projetos elétricos de baixa e alta tensão (13,8 a 230 kV), diagramas unifilares, projetos de montagem eletromecânica, projetos funcionais de painéis, diagramas de interligação, lista de materiais, memoriais de cálculo, memoriais descritivos, quadros de carga, laudos de aterramento, entre outros documentos relacionados a subestações de energia',
                            place: {
                                name: 'Engeserve Engenharia e Serviços Ltda',
                                acronym: '',
                                image: {
                                    logo: 'assets/img/engeserve.png',
                                    icon: 'assets/img/engeserve.png',
                                },
                                page_url: 'http://www.engeserve.com.br/',
                                parents: [],
                            },
                            position: 'Estágio em Engenheiro Elétrica',
                            location: 'Goiânia, GO',
                            year: {
                                start: '2011',
                                end: '2013'
                            }
                        },
                        {
                            description: 'Experiência como funcionário de uma franquia internacional com o objetivo de desenvolver o idioma inglês, obrigatório na época para todos os funcionários de contato direto com clientes, além de auxiliar com os custos existentes durante o período de graduação',
                            place: {
                                name: 'Outback Steak House Goiânia',
                                acronym: '',
                                image: {
                                    logo: 'assets/img/outback.png',
                                    icon: 'assets/img/outback.png',
                                },
                                page_url: 'https://www.outback.com.br/',
                                parents: [
                                    {
                                        name: 'Flamboyant Shopping',
                                        acronym: '',
                                        image: {
                                            logo: 'assets/img/flamboyant.png',
                                            icon: 'assets/img/flamboyant.png',
                                        },
                                        page_url: 'http://www.flamboyant.com.br/',
                                    },
                                ],
                            },
                            position: 'Waiter (Atendente)',
                            location: 'Goiânia, GO',
                            year: {
                                start: '2009',
                                end: '2010'
                            }
                        },
                        {
                            description: 'Trabalho exercido como membro da equipe responsável por auxiliar clientes com a instalação e configuração, de maneira remota, de modens CDMA e GSM (GPRS/HSPDA) e configuração de informações de ISP da operadora nos computadores Windows, MacOS/OSX e Linux durante a fase de implantação da tecnologia 3G da Vivo S/A. no Brasil',
                            place: {
                                name: 'Atento Brasil Ltda',
                                acronym: '',
                                image: {
                                    logo: 'assets/img/atento.png',
                                    icon: 'assets/img/atento.png',
                                },
                                page_url: 'http://atento.com/locations/brazil/',
                                parents: [
                                    {
                                        name: 'Vivo Brasil S/A',
                                        acronym: 'https://www.vivoempresas.com.br/‎',
                                        image: {
                                            logo: 'assets/img/vivo.png',
                                            icon: 'assets/img/vivo.png',
                                        },
                                        page_url: '',
                                    },
                                ],
                            },
                            position: 'Atendente direto para consumidores Pessoa Jurídica',
                            location: 'Goiânia, GO',
                            year: {
                                start: '2008',
                                end: '2009'
                            }
                        },
                    ]
                },
            }
        },
        methods: {
            getGithubData(username) {

                let url = 'https://api.github.com/users/'+username;
                axios.get(url)
                .then(res => { 
                    this.data.github.user = res.data;
                });

                let repos = [];
                this.data.github.repos.forEach(function (repo) {
                    let repo_url = 'https://api.github.com/repos/'+username+'/'+repo.name;
                    axios.get(repo_url)
                    .then(res => { repos.push(res.data) })
                });
                this.data.github.repos = repos;

                let orgs_url = url+'/orgs';
                axios.get(orgs_url)
                .then(res => { 
                    let orgs = [];
                    res.data.forEach(function (org) { 
                        let org_url = 'https://api.github.com/orgs/'+org.login;
                        axios.get(org_url)
                        .then(res => {
                            // console.log(res.data);
                            orgs.push(res.data);
                        });
                    });
                    this.data.github.orgs = orgs;
                });

                // [this.data.github.orgs].forEach(function (org) { console.log(org); });

                // let teste = function() {
                //     for (var org in this.data.github.orgs) {
                //         console.log('trying'+org)
                
                //     };
                // }
            },
        },
        created: function() {
            this.getGithubData(this.data.github.username);
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










