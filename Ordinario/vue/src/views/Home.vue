<template>
  <div class="home">
    <!-- Muestra imagen -->
    <img src="@/assets/bookstore.jpg" class="img-fluid" alt="Responsive image" width="604" height="236" text-align="center">
    <Footer></Footer>
  </div>
</template>

<script>
// @ is an alias to /src
import Footer from '@/components/Footer.vue'

export default {
  name: 'Home',
  components: {
    Footer
  }
  
}
</script>