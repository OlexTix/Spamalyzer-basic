<template>
    <div class="flex h-screen w-screen bg-gray-50">
      <!-- Sidebar -->
      <Sidebar class="basis-1_6 lg:basis-1_5 border-r bg-white" />
  
      <!-- Mail List -->
      <MailList class="basis-2_6 lg:basis-2_5 border-r bg-gray-100" @select-mail="selectMail" />
  
      <!-- Mail Details -->
      <MailDetails class="flex-1 bg-white" :selected-mail="selectedMail" />
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import Sidebar from "@/components/Sidebar.vue";
  import MailList from "@/components/MailList.vue";
  import MailDetails from "@/components/MailDetails.vue";
  
  const selectedMail = ref(null);
  
  const selectMail = (mail) => {
    selectedMail.value = mail;
  };
  </script>
  
  <style scoped>

  .basis-1_6 {
    flex-basis: 16.666667%;
  }
  
  .basis-1_5 {
    flex-basis: 20%;
  }
  
  .basis-2_6 {
    flex-basis: 33.333333%;
  }
  
  .basis-2_5 {
    flex-basis: 40%;
  }
  

  @media (max-width: 1024px) {
    .basis-1_6 {
      flex-basis: 20%;
    }
  
    .basis-2_6 {
      flex-basis: 40%;
    }
  }
  </style>
  