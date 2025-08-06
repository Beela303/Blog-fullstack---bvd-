<script>
  import Menu from '@/components/Menu.vue'
  import { RouterLink, RouterView } from 'vue-router'

  export default {
    components: {
      Menu,
    }
  }
</script>

<template>
  <Menu />
  <RouterView />
</template>

<style>
a {
  text-decoration: none;
}

.row{
  width: 100% !important;
}
</style>
