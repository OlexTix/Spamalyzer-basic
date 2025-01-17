<template>
    <div class="p-6 h-full overflow-y-auto">
      <h2 class="text-lg font-bold mb-6">Folders</h2>
      <ul class="space-y-4">
        <li
          v-for="folder in folders"
          :key="folder"
          class="cursor-pointer p-3 hover:bg-indigo-100 rounded-md text-gray-700 font-medium"
        >
          {{ folder }}
        </li>
      </ul>
    </div>
  </template>
  
  <script setup>
  const folders = ["Inbox", "Sent", "Drafts", "Trash"];
  </script>
  
  <style scoped>
  
  h-full {
    height: 100%;
  }
  </style>
  