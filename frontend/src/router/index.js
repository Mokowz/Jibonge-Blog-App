import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home/Home.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../views/SignUp/SignUpView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login/Login.vue')
  },
  {
    path: '/blogs',
    name: 'blogs',
    component: () => import('../views/Blogs/Blogs.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
