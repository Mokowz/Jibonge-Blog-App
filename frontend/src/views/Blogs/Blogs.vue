<template>
  <div class="flex flex-col container mx-auto px-4">
    <!-- Blog Header -->
     <div class="flex flex-col w-lg border-b border-darkGrey my-8 space-y-3 pb-5">
      <h1 class="text-4xl md:text-5xl font-bold">All Blogs</h1>
      <input type="search" class="mb-5 max-w-sm bg-white/10 px-4 rounded-md py-3" placeholder="Search Blogs">
     </div>

     <!-- The Blogs -->
      <Blogs />

  </div>
</template>

<script>
import Blogs from '../../components/Blogs.vue';

export default {
  components: {
    Blogs,
  }
}
</script>

<style>

</style>