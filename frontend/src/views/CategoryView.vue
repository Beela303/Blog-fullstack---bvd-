<script>
import Aside from '@/components/Aside.vue';

export default {
    components: {
        Aside,
    }
}
</script>

<template>
    <div class="row g-5">
        <div class="col-md-8">
            <h2 class="display-4 text-center">Category Name</h2>

      <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
        <div class="col p-4 d-flex flex-column position-static"> <strong
            class="d-inline-block mb-2 text-success-emphasis">Design</strong>
          <h3 class="mb-0">Post title</h3>
          <div class="mb-1 text-body-secondary">Nov 11</div>
          <p class="mb-auto">This is a wider card with supporting text below as a natural lead-in to
            additional content.</p>
            <a href="" class="btn btn-secondary">Read More...</a>
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