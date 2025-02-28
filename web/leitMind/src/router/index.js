import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
import Templateone from '../views/Templateone.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: LandingPage
  },
  {
    path: '/template',
    name: 'template',
    component: Templateone
  }
]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})

export default router
