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
  },
  {
    path: '/blog/:id',
    name: 'blog',
    component: () => import('../views/Blogs/Blog.vue')
  },
  {
    path: '/tags',
    name: 'tags',
    component: () => import('../views/Tags/Tags.vue')
  },
  {
    path: '/tags/:id',
    name: 'tagList',
    component: () => import('../views/Tags/TagBlogs.vue')
  },
  {
    path: '/authors',
    name: 'authors',
    component: () => import('../views/Authors/Authors.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
