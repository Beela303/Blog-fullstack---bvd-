<script>
import axios from 'axios';
import Aside from '@/components/Aside.vue';

export default {
    components: {
        Aside,
    },

    data() {
        return {
            categoryDetail: {},
            categoryPosts: [],
        }
    },

    mounted() {
        this.getCategoryDetail(),
        this.getCategoryPosts()
    },

    methods: {
        getCategoryDetail() {
            const category_slug = this.$route.params.category_slug

            axios
                .get(`categories/${category_slug}`)
                .then(response => {
                    this.categoryDetail= response.data 
                })
                .catch(error => {
                    console.log(error)
                })
        },

        getCategoryPosts() {
            const category_slug = this.$route.params.category_slug
            
            axios
                .get(`${category_slug}/posts`)
                .then(response => {
                    this.categoryPosts= response.data 
                })
                .catch(error => {
                    console.log(error)
                })
        },
    }
}
</script>

<template>
    <div class="row g-5">
        <div class="col-md-8">
            
            <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
                <div class="col p-4 d-flex flex-column position-static">
                <h2 class="display-4 text-center">{{ categoryDetail.name }}</h2>
                <p class="mb-auto text-center">{{ categoryDetail.description }}</p>
            </div>
            <div class="col-auto d-none d-lg-block"> 
                <img src="../assets/1.jpeg" alt="">    
            </div>
      </div>
    
      
      <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative" v-for="categoryPosts in categoryPosts" v-bind:key="categoryPosts.id">
        <div class="col p-4 d-flex flex-column position-static"> 
          <strong class="d-inline-block mb-2 text-success-emphasis">hh</strong>
          <h3 class="mb-0">{{ categoryPosts.title }}</h3>

          <div class="mb-1 text-body-secondary">{{ categoryPosts.created_on }}</div>
          <p class="mb-auto">{{ categoryPosts.content }}</p>
          <router-link :to="categoryPosts.get_absolute_url" class="btn btn-secondary">Read More...</router-link>
        </div>

        <div class="col-auto d-none d-lg-block"> 
          <img src="../assets/1.jpeg" alt="">    
        </div>
      </div>
      
    </div>

        <Aside />
    </div>
</template>

<style>
</style>