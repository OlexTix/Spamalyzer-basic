<template>
  <div class="w-full max-w-md bg-white shadow-2xl rounded-lg p-8 md:p-10">
    <div class="text-center mb-8">
      <i class="pi pi-user text-indigo-600 text-5xl"></i>
      <h2 class="mt-4 text-3xl font-extrabold text-gray-900">Spamalyzer</h2>
      <p class="mt-2 text-sm text-gray-500">Log in to your account</p>
    </div>
    <form @submit.prevent="handleSubmit" class="space-y-6">
      <!-- Email Field -->
      <div>
        <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
        <InputText
          v-model="email"
          id="email"
          type="email"
          placeholder="you@example.com"
          class="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        />
      </div>
      <!-- Password Field -->
      <div>
        <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
        <div class="relative w-full">
          <Password
            v-model="password"
            id="password"
            placeholder="••••••••"
            toggleMask
            feedback="false"
            class="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            inputClass="pr-12"
          />
          <!-- Icon inside the field -->
          <i
            class="pi pi-eye absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 cursor-pointer"
            @click="togglePasswordVisibility"
          ></i>
        </div>
      </div>
      <!-- Options -->
      <div class="flex items-center justify-between">
        <div class="flex items-center">
        
        </div>
     
      </div>
      <!-- Submit Button -->
      <Button
        type="submit"
        label="Log In"
        class="w-full p-button-rounded p-button-lg p-button-primary hover:shadow-lg transition duration-300"
      />
    </form>
    <!-- Divider -->
    <div class="flex items-center mt-6">
      <hr class="flex-1 border-gray-300" />
      <span class="px-4 text-sm text-gray-500">Or log in with</span>
      <hr class="flex-1 border-gray-300" />
    </div>
    <!-- Google Button -->
    <div class="flex mt-6 justify-center">
      <button
        class="flex items-center justify-center gap-2 px-4 py-2 bg-red-600 text-white rounded-lg shadow-md hover:bg-red-700 transition duration-300"
      >
       Google
      </button>
    </div>
    <!-- Sign-up Link -->
   
  </div>
</template>

<script setup>
import { ref } from "vue";
import InputText from "primevue/inputtext";
import Password from "primevue/password";
import Checkbox from "primevue/checkbox";
import Button from "primevue/button";

const email = ref("");
const password = ref("");
const rememberMe = ref(false);


const handleSubmit = () => {
  if (!email.value || !password.value) {
    alert("Please fill in both fields.");
    return;
  }

};
</script>

<style>
.p-inputtext.p-password-input
{

  width: 1000px;
}

a:hover {
  text-decoration: none;
  background-color: transparent;
}

</style>