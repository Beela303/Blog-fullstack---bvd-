<script>
import axios from 'axios';

export default {
    data() {
        return {
            categories: []
        }
    },

    mounted() {
        this.getCategories()
    },

    methods: {
        getCategories() {
            axios
                .get('categories/')
                .then(response => {
                    this.categories = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>

<template>
   <div class="container">
        <header class="border-bottom lh-1 py-3">
            <div class="row flex-nowrap justify-content-between align-items-center">
                <div class="col-4 pt-1"> 
                    <a class="link-secondary text-white" href="#">Subscribe</a> 
                </div>
                <div class="col-4 text-center"> 
                    <router-link to="/" class="blog-header-logo text-body-emphasis text-decoration-none text-white">
                        Blog
                    </router-link> 
                </div>
                <div class="col-4 d-flex justify-content-end align-items-center"> 
                    <a class="link-secondary text-white" href="#" aria-label="Search"> 
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none"
                            stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            class="mx-3" role="img" viewBox="0 0 24 24">
                            <title>Search</title>
                            <circle cx="10.5" cy="10.5" r="7.5"></circle>
                            <path d="M21 21l-5.2-5.2"></path>
                        </svg> 
                    </a> 
                    <a class="btn btn-sm btn-outline-secondary text-white" href="#">Sign up</a> 
                </div>
            </div>
        </header>
        <div class="nav-scroller py-1 mb-3 border-bottom">
            <nav class="nav nav-underline justify-content-between" v-for="category in categories" v-bind:key="category.id"> 
                <router-link :to="category.get_absolute_url" class="nav-item nav-link link-body-emphasis text-white" exact-active-class="active">{{ category.name }}</router-link>
            </nav>
        </div>
    </div>
</template>

<style scoped>

</style>