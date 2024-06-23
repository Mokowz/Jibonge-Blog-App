<template>
  <div class="flex flex-col container mx-auto">
    <!-- Header -->
     <div class="text-center font-bold text-4xl border-b w-full border-darkGrey py-4">
        <h1>{{ blog.title }}</h1>
     </div>

    <!-- Rest -->
     <div class="flex mt-6  justify-between">
      <!-- Side Profile -->
       <div class="flex flex-col space-y-4 w-1/5">
        <!-- Author -->
        <div class="border-b border-darkGrey py-3 px-1">
          <h1 class="font-bold text-yellow-500 text-xl mb-2">Author</h1>
          <span>By {{ blog.author }}</span>
        </div>
        <div class="border-b border-darkGrey py-3 px-1">
          <h1 class="font-bold text-xl text-yellow-500 mb-2">Tags</h1>
          <span v-for="tag in blog.tags" :key="tag" class="mr-3">{{ tag.name }}</span>
        </div>
        <div class="border-b border-darkGrey py-3 px-1">
          <router-link to="/blogs" class="text-yellow-500"> << Back to Blogs</router-link>
        </div>
       </div>

       <!-- Content -->
       <div class="px-10 py-8 w-4/5">
          <p class="text-darkGrey">{{ blog.content }}</p>
       </div>

     </div>
  </div>
</template>

<script>
import axios from 'axios';
import { apiBaseUrl } from '@/config';

export default {
  props: {
    id: {
      type: String,
      required: true
    }
  }
  ,

  data() {
    return {
      blog: []
    }
  },

  created() {
    this.fetchBlog()
  },

  methods: { 
    async fetchBlog() {
      const response = await axios.get(`${apiBaseUrl}blogs/${this.$route.params.id}/`)
                      .then((response) => {
                        this.blog = response.data;
                      })
    }
  }
}
</script>

<style>

</style>