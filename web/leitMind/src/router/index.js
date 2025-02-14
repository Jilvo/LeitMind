import { createRouter, createWebHistory } from 'vue-router'

import TemplateOne from '../views/TemplateOne.vue'

const routes = [
  {
    path: '/',
    name: 'TemplateOne',
    component: TemplateOne
  },
]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})

export default router
