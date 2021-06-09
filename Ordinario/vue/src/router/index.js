import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import (/* webpackChunkName: "home" */ '../views/Home.vue')
  },
  {
    path: '/library',
    name: 'library',
    component: () => import (/* webpackChunkName: "servicios" */ '../views/Library.vue')
  },
  {
    path: '/book',
    name: 'book',
    component: () => import (/* webpackChunkName: "book" */ '../views/Book.vue')
  },
  {
    path: '/book/:id',
    name: 'bookid',
    component: () => import (/* webpackChunkName: "bookid" */ '../views/BookId.vue')
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
