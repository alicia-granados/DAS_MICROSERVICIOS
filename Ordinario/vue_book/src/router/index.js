import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/CRUD_Book',
    name: 'CRUD_Book',
    component: () => import(/* webpackChunkName: "CRUD_Book" */ '../views/CRUD_Book.vue')
  },
  {
    path: '/bookup/:id',
    name: 'bookidup',
    component: () => import (/* webpackChunkName: "bookid_update */ '../views/BookId_Update.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router

