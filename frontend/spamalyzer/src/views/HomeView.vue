<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import Button from "primevue/button";
import Textarea from "primevue/textarea";
import lottie from "lottie-web"; // Import Lottie library

const email = ref("");
const classificationResult = ref(null);
const isLoading = ref(false);
const showInstructions = ref(true); // Show instructions initially

const headerAnimationContainer = ref(null);
const processingAnimationContainer = ref(null);
const isSpam = ref(false);

// Import Lottie animation JSON files
import envelopeAnimation from "@/assets/animations/mail.json";
import mailProcessingAnimation from "@/assets/animations/mail2.json";

let processingAnimationInstance = null;

const classifyEmail = async () => {
  if (!email.value.trim()) {
    classificationResult.value = "Please enter a valid email text.";
    return;
  }

  classificationResult.value = null;
  isLoading.value = true;
  showInstructions.value = false; // Hide instructions when processing starts

  if (processingAnimationInstance) {
    processingAnimationInstance.play();
  }

  try {
    const response = await axios.post("https://nlpfastify.lhmngr.pl/classify", {
      emailText: email.value,
    });

    if (response.status === 204) {
      classificationResult.value = "This email is NOT SPAM.";
      isSpam.value = false;
    } else if (response.status === 200) {
      classificationResult.value = "This email has been classified as SPAM.";
      isSpam.value = true;
    }
  } catch (error) {
    classificationResult.value = "Error: Unable to classify the email.";
    console.error("API error:", error);
  } finally {
    isLoading.value = false;

    if (processingAnimationInstance) {
      processingAnimationInstance.stop();
    }
  }
};

const resetClassifier = () => {
  email.value = "";
  classificationResult.value = null;
  showInstructions.value = true; // Show instructions again
};

const confirmSpam = () => {
  console.log("Confirmed as SPAM: ", email.value);
  resetClassifier();
};

// Initialize Lottie animations
onMounted(() => {
  lottie.loadAnimation({
    container: headerAnimationContainer.value,
    renderer: "svg",
    loop: true,
    autoplay: true,
    animationData: envelopeAnimation,
  });

  processingAnimationInstance = lottie.loadAnimation({
    container: processingAnimationContainer.value,
    renderer: "svg",
    loop: true,
    autoplay: false,
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
        <p class="text-gray-600 text-lg font-semibold mb-6 text-center">
          Enter an email text below to classify whether it is SPAM or not.
        </p>
        <Textarea
          v-model="email"
          rows="8"
          placeholder="Enter email text here..."
          class="w-full p-4 text-xl border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500 mb-6"
        />
        <Button
          label="Classify Email"
          class="btn-primary w-full text-lg"
          @click="classifyEmail"
        />
      </div>

      <!-- Loading Section -->
      <div v-show="isLoading" class="flex items-center justify-center flex-col">
        <div ref="processingAnimationContainer" class="w-48 h-48"></div>
        <p class="text-gray-600 text-lg mt-4">Processing your email...</p>
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
              'text-red-500 animate-pulse': isSpam,
              'text-green-500': !isSpam,
            }"
          >
            {{ classificationResult }}
          </p>
          <div v-if="isSpam" class="mt-6">
            <Button
              label="Confirm SPAM"
              class="p-button-rounded p-button-danger w-40 mr-4"
              @click="confirmSpam"
            />
            <Button
              label="Not SPAM"
              class="p-button-rounded p-button-success w-40"
              @click="resetClassifier"
            />
          </div>
          <div v-else>
            <Button
              label="Classify Another Email"
              class="btn-primary w-full mt-4"
              @click="resetClassifier"
            />
          </div>
        </div>
      </Transition>
    </div>

    <!-- Instructions Section -->
    <Transition name="slide-down">
      <div
        id="instructions"
        v-show="showInstructions"
        class="instructions-section"
      >
        <h2 class="text-2xl font-bold text-indigo-700 mb-4 text-center">Instructions</h2>
        <ul class="list-disc pl-6 text-gray-700 text-lg">
          <li>Only emails in English are supported for classification.</li>
          <li>Provide full email content, including subject and body.</li>
          <li>The email text should not include sensitive personal information.</li>
          <li>Ensure the email text is clear and free from unnecessary formatting.</li>
        </ul>
      </div>
    </Transition>
  </main>
</template>

<style scoped>

.btn-primary:hover {
  transform: scale(1.02);
}


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
  animation: shine 4s linear infinite;
}

@keyframes shine {
  0% {
    background-position: 200% center;
  }
  100% {
    background-position: -200% center;
  }
}


.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}


.instructions-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
  background: rgba(255, 255, 255, 0.9);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.2);
}


.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.3s ease;
}
.slide-down-enter-from {
  transform: translateY(-20px);
  opacity: 0;
}
.slide-down-leave-to {
  transform: translateY(-20px);
  opacity: 0;
}

[v-show="false"] {
  display: none;
}
</style>
