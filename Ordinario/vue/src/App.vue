<template>
  
  <div id="app" class="container">
    <div id="nav">
    
      <router-link  class="navbar-brand"  to="/">Home</router-link>  <!-- Returns to the "Home" view -->
      <router-link  class="navbar-brand" to="/library">Library</router-link>  <!-- Returns to the "Library" view -->
      <router-link  class="navbar-brand" to="/book">Insert</router-link> <!-- Returns to the "Instert" view -->
      <router-view/>
    </div>    
  </div>
</template>

<style> 
  /* Adds styles to HTML */
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;

  }
  #nav {
    padding: 30px;
  }

  #nav a {
    font-weight: normal;
    color: #f02a68;
      font-size:130%
  }
  
</style>


