<script>
import axios from 'axios';
import Aside from '@/components/Aside.vue';

export default {
    components: {
        Aside,
    },

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
    <div class="row g-5">
        <div class="col-md-8">
            <h2 class="display-4 text-center">Categories</h2>

            <div class="container">
                <div class="row" v-for="categories in categories" v-bind:key="categories.id">

                    <div class="col-md-6 mb-4">
                        <router-link to="">
                            <div class="card">
                                <img src="../assets/1.jpeg" alt="" class="card-img-top">
                                <div class="card-body">
                                    <h5 class="card-title text-center">{{ categories.name }}</h5>
                                    <p class="card-title">{{ categories.description }}</p>
                                </div>
                            </div>
                        </router-link>
                    </div>

                </div>
            </div>
        </div>

        <Aside />
    </div>
</template>

<style>
.card img {
    height: 200px;
    object-fit: cover;
}
</style>