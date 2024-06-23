<template>
  <form action="" class="flex flex-col mt-5">
    <input type="text" name="first-name" v-model="first_name" class="mb-5 bg-white/10 px-4 rounded-sm py-3" placeholder="First Name">
    <input type="text" name="last-name" v-model="last_name" class="mb-5 bg-white/10 px-4 rounded-sm py-3" placeholder="Last Name">
    <input type="email" name="email" v-model="email" class="mb-5 bg-white/10 px-4 rounded-sm py-3" placeholder="Email">
    <input type="password" name="password" v-model="password" class="mb-5 bg-white/10 px-4 rounded-sm py-3" placeholder="Password">
    <input type="password" name="confirmPassword" v-model="confirmPassword" class="mb-5 bg-white/10 px-4 rounded-sm py-3" placeholder="Confirm Password">
    <input type="submit" class="mb-5 bg-yellow-500 px-4 rounded-sm py-3" value="Sign Up">
  </form>
</template>

<script>
import axios from 'axios';
import { apiBaseUrl } from '../../config';

export default {
  data() {
    return {
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      confirmPassword: ''
    }
  },

  methods: {
    async signup() {
      const response = axios.post(`${apiBaseUrl}register/`, {
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
        password: this.password,
        password2: this.confirmPassword
      })

      if (response.status === 201) {
        this.$router.push('/login')
      }
    }
  }
}
</script>

<style>

</style>