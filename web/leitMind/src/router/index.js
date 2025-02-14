import { createRouter, createWebHistory } from 'vue-router'

import Templateone from '../views/Templateone.vue'

const routes = [
  {
    path: '/',
    name: 'TemplateOne',
    component: Templateone
  },
]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})

export default router
