<template>
  <nav class="w-full  text-white mb-5">
    <div class="flex container mx-auto items-center px-3 py-5 flex-row justify-between">
      <!-- Logo -->
      <router-link to="/" class="text-3xl font-riot font-bold">Ji<span class="font-riot text-yellow-500">Bonge</span></router-link>

       <!-- Nav Menu  -->
      <div class="text-lg/3  flex items-center">
        <router-link to="/blogs" class="mr-6 hover:underline">Blogs</router-link>
        <router-link to="/" class="mr-6 hover:underline">Authors</router-link>
        <router-link to="/" class="mr-6 hover:underline">Tags</router-link>

        <!-- Sign Up page / Login Page -->
        <router-link to="/signup" class="mr-6 hover:underline">Sign Up</router-link>
        <router-link to="/login" class="mr-6 hover:underline">Log In</router-link>
      </div>

    </div>
  </nav>
</template>

<script>
export default {

}
</script>

<style>

</style>