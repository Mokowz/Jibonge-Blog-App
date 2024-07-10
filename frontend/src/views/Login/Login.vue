<template>
  <!-- Sign Up Page -->
  <div class="flex container mx-auto justify-center items-center">


    <!-- Form Card -->
     <div class="flex flex-col px-5 py-6 border border-darkGrey rounded-sm">
        <!-- Header -->
        <div class="text-center">
          <h1 class="text-yellow-500 font-semibold text-2xl">Log In</h1>
          <p>Welcome Back Mkuu</p>
        </div>

        <!-- Form -->
         <LoginForm />

         <!-- Or Login -->
          <span class="text-center">
            Ama hauna account? <router-link to="/signup" class="text-yellow-500">Sign Up</router-link>
          </span>

     </div>

  </div>
</template>

<script>
import LoginForm from './LoginForm.vue'


export default {
  components: {
    LoginForm,
  }
}
</script>

<style>

</style>