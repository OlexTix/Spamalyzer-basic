<template>
    <div class="p-6 h-full overflow-y-auto">
      <div v-if="selectedMail">
        <h2 class="text-xl font-bold text-gray-900 mb-4">{{ selectedMail.subject }}</h2>
        <p class="text-sm text-gray-600 mb-4">From: {{ selectedMail.sender }}</p>
        <hr class="mb-6" />
        <p class="text-gray-700">{{ selectedMail.content }}</p>
      </div>
      <div v-else class="flex items-center justify-center h-full text-gray-400 text-lg">
        Select a message to read
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from "vue";
  
  defineProps({
    selectedMail: {
      type: Object,
      required: false,
    },
  });
  </script>
  