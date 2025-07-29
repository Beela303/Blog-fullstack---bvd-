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
        }
    },

    mounted() {
        this.getCategoryDetail()
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
    </div>

        <Aside />
    </div>
</template>

<style>
</style>