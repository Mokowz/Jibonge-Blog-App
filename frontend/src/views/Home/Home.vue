<template>
  <div class="flex flex-col px-4 container mx-auto mt-20">
    <!-- Header -->
     <div class="border-b pb-5 border-darkGrey">
      <h1 class="text-4xl md:text-5xl font-bold mb-5">Karibu Jibonge, a one-stop <h1 class="text-yellow-500">magazine</h1> 
        for all you Swahili and sheng lovers</h1>

      <p class="text-darkGrey">Jibonge offers a vibrant space where Swahili and Sheng aficionados can delve into
         a diverse array of content. From language insights to cultural
          explorations, it's your go-to platform for immersive experiences and
           community connections in the realm of East 
           African languages.
      </p>
     </div>

     <!-- Posts -->
      <Blogs :search="field" />

      <router-link to="/blogs" class="text-yellow-500 my-5 text-lg">All Posts >></router-link>

  </div>
</template>

<script>
import Blogs from '@/components/Blogs.vue'

export default {
  components: {
    Blogs,
  },

  data() {
    return {
      field: ''
    }
  }
}
</script>

<style>

</style>