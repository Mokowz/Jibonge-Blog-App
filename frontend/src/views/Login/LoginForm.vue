<template>
  <form action="" @submit.prevent="login" class="flex flex-col mt-5">
    <input type="email" v-model="email" name="email" class="mb-5 bg-white/10 px-4 rounded-sm py-3" placeholder="Email">
    <input type="password" v-model="password" name="password" class="mb-5 bg-white/10 px-4 rounded-sm py-3" placeholder="Password">
    <input type="submit" class="mb-5 cursor-pointer bg-yellow-500 px-4 rounded-sm py-3" value="Log In">
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      loggedIn: false,
    }
  },

  methods: {
    async login() {
      const response = await axios.post('http://54.144.151.102/api/v1/token/', {
          email: this.email,
          password: this.password
      })

      if (response.status === 200) {
        this.loggedIn = true;
        this.$router.push('/')
      }
      
    }
  },

}
</script>

<style>

</style>