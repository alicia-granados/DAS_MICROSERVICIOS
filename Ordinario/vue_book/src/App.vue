<template>
  <v-app>
    <Navbar></Navbar>
    <v-container>
      <v-main>
      <router-view/>
    </v-main>
    </v-container>
    
  </v-app>
</template>

<script>

  import Navbar from './components/Navbar.vue';

  export default {
    name: 'App',
    components:{
      Navbar
    },
    data: () => ({
      //
    }),
  };

</script>
