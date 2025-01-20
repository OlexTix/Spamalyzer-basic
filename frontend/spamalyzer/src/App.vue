<script setup>
import { RouterView } from 'vue-router';
</script>

<template>
  <div class="app-container">
    <RouterView />
  </div>
</template>

<style scoped>
.app-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  padding: 0;
  background-color: #f3f4f6; /* Neutralne tło */
}
</style>
