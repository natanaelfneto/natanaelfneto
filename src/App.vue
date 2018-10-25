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
                    activeTab: 'Published',
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
                    published: [
                        {
                            description: 'Paper documents are being replace in different areas every day and, for any activity that requires authenticity, these new digital forms need to assure the same guaranties as the physical document does, i.e., authorship, authenticity, chronological evidence and integrity. In this article we shall analyze a viable use of available technologies to solve this evidenced issue. In medical reports for image exams, the use of a Picture Archive Communications System (PACS) allow the medical reports to be emitted remotely but it alone does not guarantee any of the security measurements for non-repudiation. The results presented in this article were obtained from an Integrative Literature Review and make evidence that the digital signatures model, based on asymmetric cryptography, could help solve this issue if a solution implementation does not change the installed DICOM/PACS environment and if it makes possible for an easy emitter check without the possibility of repudiation, within the local legislation',
                            preview: '',
                            sources: [
                                {
                                    type: 'link',
                                    icon: 'fa_ fa-link',
                                    link: 'https://periodicos.ufersa.edu.br/index.php/ecop/article/view/7901',
                                },
                                {
                                    type: 'pdf',
                                    icon: 'far fa-file-pdf',
                                    link: 'https://periodicos.ufersa.edu.br/index.php/ecop/article/view/7901/6958',
                                },
                            ],
                            work: 'Digital Signatures Schemes: An Integrative Literature Review of Asymmetric Cryptography Usage as a Technical Method for Authenticity and Nonrepudiation on Remote Medical Reports for PACS',
                            appends: '',
                            type: 'Article',
                            authors: [
                                {
                                    name: 'Freitas Neto, N.',
                                },
                                {
                                    name: 'Freitas, M. A. N.',
                                },
                                {
                                    name: 'Dantas, M. C. R.',
                                },
                                {
                                    name: 'Valentim, R. A. M.',
                                }
                            ],
                            location: {
                                name: 'ECOP/UFERSA',
                                is: {
                                    sn: '2526-7574',
                                    bn: '',
                                },
                                link: 'https://periodicos.ufersa.edu.br/index.php/ecop/article/view/7901',
                            },
                            year: '2018',
                        },
                        {
                            description: 'O Sistema Único de Saúde (SUS) representa uma das principais conquistas da sociedade brasileira e tem sido referenciado como sendo um dos maiores sistemas de saúde pública do mundo. Afinal, ele é responsável por ações que vão desde a promoção da saúde à atenção a doenças que exigem um alto nível de complexidade tecnológica, realizando atendimento de caráter universal. Considerando a importância da existência de um sistema de saúde com essas dimensões, vê-se necessário ressaltar o desafio de serem desenvolvidas ações educativas no âmbito do SUS tendo em vista seu fortalecimento e o aperfeiçoamento constante da sua força de trabalho. Nessa perspectiva, reconhece-se a área de Gestão do Trabalho e da Educação na Saúde como estratégica para a gestão do SUS, considerando que a coordenação da Política de Educação Permanente do trabalhador deve ser de sua responsabilidade. Por conseguinte, defende-se que ao utilizar a educação como ferramenta estratégica para a gestão, esta seja compreendida como mediadora no processo em que se relacionam o trabalho concreto e as aprendizagens subjetivas e sociais (RAMOS, 2011). É fato que a execução da Política de Educação Permanente tem se concretizado por meio de várias iniciativas, entre elas, a Educação a Distância. Que, para Belloni (2012), surge como caminho incontornável, como uma nova solução de melhoria da qualidade do ensino no sentido de adequá-lo ao século XXI',
                            preview: '',
                            sources: [
                                {
                                    type: 'link',
                                    icon: 'fa_ fa-link',
                                    link: 'http://www.observatoriorh.ufrn.br/biblioteca/categoria/11',
                                },
                                {
                                    type: 'pdf',
                                    icon: 'far fa-file-pdf',
                                    link: 'http://www.observatoriorh.ufrn.br/uploads/989ca41953558a5e3657c76432bbef71.pdf',
                                },
                            ],
                            work: 'Um olhar sobre a evasão na Educação a Distância: Para além dos números [A integração entre o ensino e o serviço de saúde: relato de atores, olhar de investigadores]',
                            appends: '1ed.Natal: Una, 2017, v. 1, p. 119-132.',
                            type: 'Book Chapter',
                            authors: [
                                {
                                    name: 'Costa, T. P. T.',
                                },
                                {
                                    name: 'Freitas Neto, N.',
                                },
                                {
                                    name: 'Castro, J. L.',
                                },
                            ],
                            location: {
                                name: 'NESC/UFRN',
                                is: {
                                    sn: '',
                                    bn: '978-85-60036-35-6',
                                },
                                link: 'http://www.observatoriorh.ufrn.br/biblioteca/categoria/11',
                            },
                            year: '2018',
                        },
                        {
                            description: 'O trabalho  descreve uma  ferramenta  Web  que permitirá  aos profissionais  da  saúde  gerenciar  formulários  de  triagem médica  com  segurança  e  dinamismo  que  não  se  consegue atualmente com  a utilização formulários em papel. A  prática  de  triagem  surgiu  das  exigências  da  guerra,  e  se mantêm intimamente associado à medicina militar. Os sistemas mais  antigos,  projetados  para  distribuir  cuidados  de  saúde sistematicamente  entre  os  soldados  feridos  e  doentes, remontam  apenas  ao  século  18  (Iserson  KV,  Moskop  JC, 2007).  No  século  21,  a  utilização  da  informática  cresce constantemente  em  diversas  áreas  do  conhecimento,  mesmo quando  elas  não  percebem,  asseverando  assim  a  natureza multidisciplinar e estratégica dessa área. O uso da informática se  torna  relevante  por  lidar  com  recursos,  dispositivos  e métodos  para  otimizar o  gerenciamento  das  informações em saúde (SBIS, 2013). O sistema desenvolvido tem por finalidade incorporar aos procesos de triagens médicas para os diferentes profissionais  envolvidos,  digitalmente,  a  criação,  atualização através  de  versionamento,  correlação  lógicas  dos  itens questionados e segurança dos dados.',
                            preview: '',
                            sources: [
                                {
                                    type: 'link',
                                    icon: 'fa_ fa-link',
                                    link: 'https://www.researchgate.net/application.ClientValidation.html?origPath=/profile/Marcel_Dantas/publication/314229421_Ferramenta_Web_para_gerar_e_gerenciar_formularios_de_triagem_medica_para_o_Hospital_Universitario_Onofre_Lopes_HUOLUFRN/links/58eabec10f7e9b978f840bf4/Ferramenta-Web-para-gerar-e-gerenciar-formularios-de-triagem-medica-para-o-Hospital-Universitario-Onofre-Lopes-HUOL-UFRN.pdf',
                                },
                                {
                                    type: 'pdf',
                                    icon: 'far fa-file-pdf',
                                    link: 'http://www.sbis.org.br/biblioteca_virtual/cbis/Anais_CBIS_2016_Diversos.pdf',
                                },
                            ],
                            work: 'Ferramenta Web para gerar e gerenciar formulários de triagem médica para o Hospital Universitário Onofre Lopes HUOL/UFRN',
                            appends: 'Goiânia. acervo da Sociedade Brasileira de Informática em Saúde, 2016.',
                            type: 'Essay',
                            authors: [
                                {
                                    name: 'Freitas Neto, N.',
                                },
                                {
                                    name: 'Freitas, I. M. A.',
                                },
                                {
                                    name: 'Guerra, P. V.',
                                },
                                {
                                    name: 'Dantas, M. C. R.',
                                },
                                {
                                    name: 'Valentim, R. A. M.',
                                }
                            ],
                            location: {
                                name: 'XV Congresso Brasileiro de Informática em Saúde',
                                is: {
                                    sn: '2178-2857',
                                    bn: '',
                                },
                                link: 'http://www.sbis.org.br/cbis2016',
                            },
                            year: '2016',
                        },
                    ],
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










