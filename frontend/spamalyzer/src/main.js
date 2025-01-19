import './assets/main.css'
import './index.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Aura from '@primevue/themes/aura';
import Vue3Lottie from 'vue3-lottie'

import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';

const app = createApp(App)

app.use(Vue3Lottie)
app.use(createPinia())
app.use(router)
app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});
app.mount('#app')
