<template>
  <NavBar    
  />
  <router-view />

 
</template>

<script>

import NavBar from './components/Navigation/NavBar.vue';

export default {
    name: 'App',
    
    components: {
        NavBar,
      
    },

    
};
</script>

<style>

</style>
