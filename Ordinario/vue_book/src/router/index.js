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
    path: '/Tarea_crud',
    name: 'Tarea_crud',
    component: () => import(/* webpackChunkName: "tarea_crud" */ '../views/CRUD_Book.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router

