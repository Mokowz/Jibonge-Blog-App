<template>
  <nav class="w-full  text-white mb-5">
    <div class="flex container mx-auto items-center px-4 md:px-3 py-5 flex-row justify-between">
      <!-- Logo -->
      <router-link to="/" class="text-3xl font-riot font-bold">Ji<span class="font-riot text-yellow-500">Bonge</span></router-link>

       <!-- Nav Menu  -->
      <div @click="changeShow()" class="text-lg/3 absolute w-full h-full md:h-auto md:w-auto top-20 md:my-auto md:static pl-6  md:pl-0 md:flex md:items-center duration-100 ease-in-out" :class="[show ? 'left-0' : 'left-[-100%]']">
        <router-link to="/blogs" class="block mb-10 mr-6 hover:underline">Blogs</router-link>
        <router-link to="/authors" class="block mb-10 mr-6 hover:underline">Authors</router-link>
        
        <router-link to="/tags" class="block mb-10 mr-6 hover:underline">Tags</router-link>

        <!-- Sign Up page / Login Page -->

        <router-link v-if="!loggedIn" to="/signup" class="block mb-10 mr-6 hover:underline">Sign Up</router-link>
        <router-link v-if="!loggedIn" to="/login" class="block mb-10 mr-6 hover:underline">Log In</router-link>
        <button v-if="loggedIn" @click="logout" class="block mb-10 mr-6 hover:underline">Log Out</button>
      </div>

      <div class="md:hidden" @click="changeShow()">
        <i :class="[show ? 'bi-x' : 'bi-list']"  class="bi text-4xl font-light"></i>
      </div>

    </div>
  </nav>
</template>

<script>
import { mapState, mapMutations } from 'vuex';

export default {
  computed: {
    ...mapState(['loggedIn']),
  },

  data() {
    return {
      show: false
    }
  },

  methods: {
    ...mapMutations(['clearAuth']),

    logout() {
      this.clearAuth()
      this.$router.push('/login')
    },

    changeShow() {
      this.show = !this.show
      document.body.style.overflowY = this.show ? 'hidden' : 'auto';
    },
  }

}
</script>

<style>

</style>