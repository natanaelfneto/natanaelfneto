<template>
    <div id="cp-sidebar-left">

        <div class="headline-v2"><h2>Formação Acadêmica</h2></div>
        <ul class="list-unstyled blog-trending margin-bottom-50">
            <li>
                <h3>
                    <span class="badge badge-secondary">MSc</span>
                    <a href="#">Ciência, Tecnologia e Inovação</a></h3>
                <small>Departamento de Ciência e Tecnologia</small>
                <small><b>2018</b> - Universidade Federal do Rio Grande do Norte</small>
            </li>
            <li>
                <h3>
                    <span class="badge badge-secondary">Esp</span>
                    <a href="#">Informática em Saúde</a></h3>
                <small>Departamento de Engenharia Biomédica</small>
                <small><b>2017</b> - Universidade Federal do Rio Grande do Norte</small>
            </li>
            <li>
                <h3>
                    <span class="badge badge-secondary">BEng</span>
                    <a href="#">Engenharia Elétrica</a></h3>
                <small>Escola de Engenharia Elétrica, Mecânica e de Computação</small>
                <small><b>2015</b> - Universidade Federal de Goiás</small>
            </li>
        </ul>

        <div class="headline-v2"><h2>Github Profile</h2></div>
        <ul class="list-unstyled">
            <h3><small>Organizações</small></h3>
            <li class="mb-4">
                <div class="row mb-2" v-for="org in data.github.orgs">
                    <a href="#" class="col-md-2 my-auto">
                        <i 
                            data-toggle="tooltip"
                            data-placement="bottom" 
                            v-bind:title="org.login"
                            v-bind:style="{ 'background-image': 'url(' + org.avatar_url + ')' }"></i>
                    </a>
                    <a href="#" class="col">
                        <span class="">{{ org.name }}</span>
                    </a>
                </div>
            </li>
            <h3><small>Repositórios Open Source</small></h3>
            <li class="mb-4">
                <div class="row mb-2" v-for="repo in data.github.repos">
                    <span class="col-md-6 mt-auto">
                        <a 
                            class="d-block badge badge-secondary cp-font"
                            v-bind:href="repo.clone_url"
                            target="_blank">
                            <span class="align-middle">{{ repo.name }}</span>
                        </a>
                    </span>
                    <span class="col mx-auto">
                        <button 
                            class="btn btn-outline-info item w-100 py-0"
                            @click.stop.prevent="clipboardCopy(repo.clone_url)">
                            <span>
                                <small class="d-inline">clone repo</small>
                                <i aria-hidden="true" class="icon-cloud-download cp-font pl-2"></i>
                            </span>
                            
                        </button>
                    </span>
                </div>
            </li>
        </ul>

        <div class="headline-v2"><h2>Newsletter</h2></div>
        <!-- Blog Newsletter -->
        <div class="blog-newsletter">
            <p>Subscribe to our newsletter for good news, sent out every month.</p>
            <div class="input-group">
                <input type="text" class="form-control" placeholder="Email">
                <span class="input-group-btn">
                    <button class="btn-u" type="button">Subscribe</button>
                </span>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        components: {
        },
        props: {
            data: {
                type: Object,
                required: true
            }
        },
        methods: {
            clipboardCopy: function(url) {
                let CopiedObject = document.createElement("textarea");
                try {
                    CopiedObject.value = 'git clone '+url
                    CopiedObject.setAttribute('readonly', '');
                    document.body.appendChild(CopiedObject);
                    CopiedObject.select()
                    document.execCommand('copy');
                    document.body.removeChild(CopiedObject);
                } catch (err) {
                    console.log("Element value could not be copied")
                }
            },
        }
    }
</script>

<style scoped>
    small {
        display: block;
    }
    .cp-font {
        font-size: 0.8rem;
        height: 1.5rem;
    }
    ul > li > div > a > i {
        color: #555;
        width: 1rem;
        height: 1rem;
        padding: 13px;
        display: inline-block;
        background-size: 100%;
        vertical-align: middle;
        border-radius: 5px;
    }
</style>