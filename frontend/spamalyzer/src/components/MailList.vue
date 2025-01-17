<template>
    <div class="p-6 h-full overflow-y-auto">
      <h2 class="text-lg font-bold mb-6">Messages</h2>
      <ul class="space-y-4">
        <li
          v-for="mail in mails"
          :key="mail.id"
          class="cursor-pointer p-4 border rounded-md hover:bg-indigo-50"
          @click="selectMail(mail)"
        >
          <div class="flex justify-between items-center">
            <span class="font-semibold text-gray-800">{{ mail.sender }}</span>
            <span class="text-sm text-gray-500">{{ mail.time }}</span>
          </div>
          <p class="text-sm text-gray-600 font-medium mt-1">{{ mail.subject }}</p>
          <p class="text-xs text-gray-400 truncate mt-1">{{ mail.preview }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { defineEmits, ref } from "vue";
  
  const emit = defineEmits(["select-mail"]);
  
  const mails = ref([
    {
      id: 1,
      sender: "Allegro",
      subject: "Nowa wiadomość",
      preview: "Cześć, masz nową wiadomość...",
      time: "20:41",
      content: "Pełna treść wiadomości od Allegro.",
    },
    {
      id: 2,
      sender: "Google",
      subject: "Alert bezpieczeństwa",
      preview: "Zalogowano się z nowego urządzenia...",
      time: "17:22",
      content: "Pełna treść wiadomości od Google.",
    },
  ]);
  
  const selectMail = (mail) => {
    emit("select-mail", mail);
  };
  </script>
  