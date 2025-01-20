<template>
  <main
    class="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-indigo-500 via-purple-600 to-pink-500 w-full"
  >
    <!-- Header Section -->
    <div ref="headerAnimationContainer" class="w-32 h-32 mb-6"></div>

    <h1 class="spamalyzer-title">SPAMalyzer</h1>

    <!-- Main Card -->
    <div
      class="max-w-4xl w-full bg-white/10 backdrop-blur-md shadow-lg rounded-lg p-6 md:p-10 border border-white/20"
    >
      <!-- Input Section -->
      <div v-if="!classificationResult && !isLoading">
        <p class="text-gray-200 text-lg font-semibold mb-6 text-center">
          Enter an email text below to classify whether it is SPAM or not.
        </p>
        <Textarea
          v-model="email"
          rows="8"
          placeholder="Enter email text here..."
          class="textarea w-full"
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
        <p class="text-gray-200 text-lg mt-4">Processing your email...</p>
      </div>

      <!-- Result Section -->
      <Transition name="fade">
        <div v-if="classificationResult && !isLoading" class="text-center mt-6">
          <p class="result-text">
            {{ classificationResult }}
          </p>
          <div v-if="isSpam" class="flex gap-4 justify-center mt-6">
            <Button
              label="Confirm SPAM"
              class="btn-danger"
              @click="confirmSpam"
            />
            <Button
              label="Not SPAM"
              class="btn-success"
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
  </main>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import Button from "primevue/button";
import Textarea from "primevue/textarea";
import lottie from "lottie-web";

const email = ref("");
const classificationResult = ref(null);
const isLoading = ref(false);
const isSpam = ref(false);

const headerAnimationContainer = ref(null);
const processingAnimationContainer = ref(null);

import envelopeAnimation from "@/assets/animations/mail.json";
import mailProcessingAnimation from "@/assets/animations/mail2.json";

const classifyEmail = async () => {
  if (!email.value.trim()) {
    classificationResult.value = "Please enter a valid email text.";
    return;
  }

  classificationResult.value = null;
  isLoading.value = true;

  try {
    const { status } = await axios.post(
      "https://nlpfastify.lhmngr.pl/classify",
      {
        emailText: email.value,
      }
    );

    const statusMessages = {
      204: { message: "This email is NOT SPAM.", spam: false },
      200: { message: "This email has been classified as SPAM.", spam: true },
    };

    const result = statusMessages[status] || {
      message: "Error: Unable to classify the email.",
      spam: false,
    };

    classificationResult.value = result.message;
    isSpam.value = result.spam;
  } catch (error) {
    classificationResult.value = "Error: Unable to classify the email.";
    console.error("API error:", error);
  } finally {
    isLoading.value = false;
  }
};

const resetClassifier = () => {
  email.value = "";
  classificationResult.value = null;
};

const confirmSpam = () => {
  console.log("Confirmed as SPAM:", email.value);
  resetClassifier();
};

const loadLottieAnimation = (
  container,
  animationData,
  autoplay = true,
  loop = true
) => {
  return lottie.loadAnimation({
    container,
    renderer: "svg",
    loop,
    autoplay,
    animationData,
  });
};

onMounted(() => {
  loadLottieAnimation(headerAnimationContainer.value, envelopeAnimation);
  loadLottieAnimation(
    processingAnimationContainer.value,
    mailProcessingAnimation,
    false
  );
});
</script>

<style scoped>
/* Background gradient animation */
main {
  background-size: 400% 400%;
  animation: gradient-animation 15s ease infinite;
}

@keyframes gradient-animation {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

/* Title shine effect */
.spamalyzer-title {
  font-size: 3rem;
  font-weight: 800;
  background: linear-gradient(
    to right,
    rgba(255, 255, 255, 0.5),
    rgba(255, 255, 255, 0.9),
    rgba(255, 255, 255, 0.5)
  );
  -webkit-background-clip: text; /* Obsługa WebKit */
  background-clip: text; /* Standard */
  -webkit-text-fill-color: transparent; /* Obsługa WebKit */
  background-size: 200% auto; /* Ważne dla przesuwania gradientu */
  animation: shine 3s linear infinite; /* Animacja */
  text-align: center;
  margin-bottom: 2rem;
}

@keyframes shine {
  0% {
    background-position: 200% center;
  }
  100% {
    background-position: -200% center;
  }
}


/* Card styling */
.max-w-4xl {
  max-width: 900px;
  padding: 2rem;
  margin: 0 auto;
}

/* Input styles */
.textarea {
  width: 100%;
  padding: 1rem;
  font-size: 1.1rem;
  color: white;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 8px;
  transition: box-shadow 0.3s, border-color 0.3s;
  margin-bottom: 1.5rem;
}

.textarea::placeholder {
  color: rgba(255, 255, 255, 0.6);
  font-style: italic;
}

.textarea:focus {
  box-shadow: 0 0 10px rgba(255, 105, 180, 0.6);
  border-color: rgba(255, 105, 180, 0.8);
}

/* Button styles */
.btn-primary {
  background: linear-gradient(to right, #ff6bcb, #ff2994);
  border: none;
  color: white; /* Tekst domyślnie biały */
  font-weight: bold;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
  transition: transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease,
    color 0.3s ease;
  position: relative;
  z-index: 1;
  overflow: hidden;
}

/* Pseudoelement gradientu */
.btn-primary::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to right, #ff6bcb, #ff2994);
  z-index: -1;
  transition: background 0.3s ease;
  border-radius: 8px;
}

/* Hover – zachowanie koloru tekstu */
.btn-primary:hover {
  transform: scale(1.05);
  background: linear-gradient(
    to right,
    #ff3ba7,
    #ff007f
  ); /* Gradient na hover */
  box-shadow: 0px 10px 20px rgba(255, 0, 127, 0.6);
  color: white !important; /* Wymuszenie koloru tekstu */
}

/* Hover dla pseudoelementu */
.btn-primary:hover::before {
  background: linear-gradient(to right, #ff7eb5, #ff5090);
}

/* Classification result text */
.result-text {
  font-size: 2rem;
  font-weight: bold;
  background: linear-gradient(to right, #ff6bcb, #ff2994);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0px 4px 6px rgba(255, 105, 180, 0.4);
}
</style>
