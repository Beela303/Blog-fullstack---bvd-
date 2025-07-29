<script>
  import axios from 'axios';

  import Featured from '@/components/Featured.vue';
  import Aside from '@/components/Aside.vue';

export default {
  data() {
    return {
      posts: []
    }
  },

  components: {
    Featured,
    Aside,
  },

  mounted() {
    this.getBlogPosts()
  },

  methods: {
    getBlogPosts() {
      axios
        .get('posts/')
        .then(response => {
          this.posts = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<template>
  <Featured />
  <div class="row g-5">
    <div class="col-md-8">
      <h2  class="display-4 text-center">Posts</h2>
      
      <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative" v-for="post in posts" v-bind:key="post.id">
        <div class="col p-4 d-flex flex-column position-static"> 
          <strong class="d-inline-block mb-2 text-success-emphasis">hh</strong>
          <h3 class="mb-0">{{ post.title }}</h3>

          <div class="mb-1 text-body-secondary">{{ post.created_on }}</div>
          <p class="mb-auto">{{ post.content }}</p>
          <router-link :to="post.get_absolute_url" class="btn btn-secondary">Read More...</router-link>
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
.col-auto img {
  width: 250px;
  height: 250px;
}
</style>