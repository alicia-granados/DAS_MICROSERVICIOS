<template>
  <div class="home">
    <!-- Shows the main image -->
    <img src="@/assets/bookstore.jpg" class="img-fluid" alt="Responsive image" width="604" height="236" text-align="center">
    <!-- Call the label -->
    <Footer></Footer>
  </div>
</template>

<script>
// Import the component named footer
import Footer from '@/components/Footer.vue' 

export default {
  name: 'Home',
  components: { 
    Footer // Adds the component named footer
  }
  
}
</script>