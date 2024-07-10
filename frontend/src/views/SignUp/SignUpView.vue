<template>
  <!-- Sign Up Page -->
  <div class="flex container mx-auto justify-center items-center">


    <!-- Form Card -->
     <div class="mx-10 md:mx-0 flex flex-col px-5 py-6 border border-darkGrey rounded-sm">
        <!-- Header -->
        <div class="text-center">
          <h1 class="text-yellow-500 font-semibold text-2xl">Sign Up</h1>
          <p>Karibu Jibonge, bonga roho yako</p>
        </div>

        <!-- Form -->
         <SignUpForm />

         <!-- Or Login -->
          <span>
            Ama you have an account with us? <router-link to="/login" class="text-yellow-500">Login</router-link>
          </span>

     </div>

  </div>
</template>

<script>
import SignUpForm from './SignUpForm.vue'


export default {
  components: {
    SignUpForm,
  }
}
</script>

<style>

</style>