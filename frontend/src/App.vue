<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import Menu from '@/components/Menu.vue'
</script>

<template>
  <Menu />
  <RouterView />
</template>

<style>
a {
  text-decoration: none;
}
</style>
