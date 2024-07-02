import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "./style.css"
import store from '@/store'

const app = createApp(App)

app.use(router)
app.use(store)

store.dispatch('initializeAuth').then(() => {
  app.mount('#app')
})

// createApp(App).use(router).use(store).mount('#app')
