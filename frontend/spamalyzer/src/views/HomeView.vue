<script setup>
import { ref, onMounted } from "vue";
import Button from "primevue/button";
import Textarea from "primevue/textarea";
import lottie from "lottie-web"; // Import Lottie library

const email = ref("");
const classificationResult = ref(null);
const isLoading = ref(false);

// Kontenery dla dwóch różnych animacji
const headerAnimationContainer = ref(null); // Animacja nagłówka
const processingAnimationContainer = ref(null); // Animacja przetwarzania

// Import Lottie animation JSON files
import envelopeAnimation from "@/assets/animations/mail.json";
import mailProcessingAnimation from "@/assets/animations/mail2.json";

let processingAnimationInstance = null; // Zmienna dla instancji animacji przetwarzania

const classifyEmail = () => {
  if (!email.value.trim()) {
    classificationResult.value = "Please enter a valid email text.";
    return;
  }

  classificationResult.value = null;
  isLoading.value = true;

  if (processingAnimationInstance) {
    processingAnimationInstance.play();
  }

  setTimeout(() => {
    classificationResult.value =
      Math.random() > 0.5 ? "This email is SPAM." : "This email is NOT SPAM.";
    isLoading.value = false;

    if (processingAnimationInstance) {
      processingAnimationInstance.stop();
    }
  }, 2000);
};

const resetClassifier = () => {
  email.value = "";
  classificationResult.value = null;
};

// Initialize Lottie animations
onMounted(() => {
  // Animacja nagłówka
  lottie.loadAnimation({
    container: headerAnimationContainer.value,
    renderer: "svg",
    loop: true,
    autoplay: true,
    animationData: envelopeAnimation,
  });

  // Preload animacji przetwarzania
  processingAnimationInstance = lottie.loadAnimation({
    container: processingAnimationContainer.value,
    renderer: "svg",
    loop: true,
    autoplay: false, // Animacja nie zaczyna się automatycznie
    animationData: mailProcessingAnimation,
  });
});
</script>

<template>
  <main class="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-indigo-500 to-blue-600 w-full p-4">
    <!-- Header Section -->
    <div ref="headerAnimationContainer" class="w-32 h-32 mb-6"></div>

    <h1 class="text-5xl font-extrabold text-white mb-8 spamalyzer-title">
      SPAMalyzer
    </h1>

    <!-- Main Card -->
    <div class="w-full max-w-4xl bg-white shadow-xl rounded-lg p-6 md:p-10">
      <!-- Input Section -->
      <div v-if="!classificationResult && !isLoading">
        <p class="text-gray-600 mb-6 text-center">
          Enter an email text below to classify whether it is SPAM or not.
        </p>
        <Textarea
          v-model="email"
          rows="8"
          placeholder="Enter email text here..."
          class="w-full p-4 text-lg border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500 mb-6"
        />
        <Button
          label="Classify Email"
          class="w-full p-button-rounded p-button-lg p-button-primary hover:shadow-lg transition duration-300"
          style="text-decoration: none;"
          @click="() => { 
            classifyEmail(); 
          }"
        />
      </div>

      <!-- Loading Section -->
      <div v-show="isLoading" class="flex items-center justify-center flex-col">
        <div ref="processingAnimationContainer" class="w-48 h-48"></div>
        <p class="text-gray-600 mt-4">Processing your email...</p>
      </div>

      <!-- Result Section -->
      <Transition name="fade">
        <div
          v-if="classificationResult && !isLoading"
          class="text-center mt-6"
        >
          <p
            class="text-2xl font-bold"
            :class="{
              'text-red-500 animate-pulse': classificationResult.includes('SPAM'),
              'text-green-500': !classificationResult.includes('SPAM'),
            }"
          >
            {{ classificationResult }}
          </p>
          <Button
            label="Classify Another Email"
            class="w-full p-button-rounded p-button-lg p-button-primary hover:shadow-lg transition duration-300"
            style="text-decoration: none; margin-top: 20px;"
            @click="resetClassifier"
          />
        </div>
      </Transition>
    </div>
  </main>
</template>

<style scoped>
/* Efekt shine dla SPAMalyzer */
.spamalyzer-title {
  position: relative;
  background: linear-gradient(
    to right,
    rgba(255, 255, 255, 0.5) 0%,
    rgba(255, 255, 255, 0.9) 50%,
    rgba(255, 255, 255, 0.5) 100%
  );
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shine 2s linear infinite;
}

/* Kluczowe ramki dla efektu shine */
@keyframes shine {
  0% {
    background-position: 200% center;
  }
  100% {
    background-position: -200% center;
  }
}

/* Animacje dla sekcji */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

a:hover {
  background-color: transparent;
}

img.animate-bounce,
svg.animate-bounce {
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

[v-show="false"] {
  display: none;
}
</style>
