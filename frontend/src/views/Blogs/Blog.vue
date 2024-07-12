<template>
  <div class="flex flex-col container mx-auto px-4">
    <!-- Header -->
     <div class="text-center font-bold text-3xl md:text-4xl border-b w-full border-darkGrey py-4">
        <h1>{{ blog.title }}</h1>
     </div>

    <!-- Rest -->
     <div class="flex mt-6  justify-between flex-col-reverse md:flex-row">

      <!-- Side Profile -->
       <div class="grid grid-cols-2 gap-5  md:flex justify-between md:justify-normal space-y-0 md:flex-col md:space-x-0 md:space-y-4 md:w-1/5">
        <!-- Author -->
        <div class="border-b border-darkGrey py-3 px-1">
          <h1 class="font-bold text-yellow-500 text-xl mb-2">Author</h1>
          <span v-if="blog.author && blog.author.user">By {{ blog.author.user.first_name }} {{ blog.author.user.last_name }}</span>
        </div>
        <div class="border-b border-darkGrey py-3 px-1" v-if="blog.tags">
          <h1 class="font-bold text-xl text-yellow-500 mb-2">Tags</h1>
          <span v-for="tag in blog.tags" :key="tag" class="mr-3">{{ tag.name }}</span>
        </div>
        <div class="border-b border-darkGrey py-3 px-1">
          <router-link to="/blogs" class="text-yellow-500"> << Back to Blogs</router-link>
        </div>
        <div class="border-b border-darkGrey py-3 px-1">
          <button @click="deleteBlog()" class="px-3 py-2 bg-yellow-500 font-semibold rounded-sm">Delete Blog</button>
        </div>
       </div>

       <!-- Content -->
       <div class="md:px-10 py-8 md:w-4/5">
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
    },

    async deleteBlog() {
      const response = await axios.delete(`${apiBaseUrl}blogs/${this.$route.params.id}/`)

      if (response.status == 204) {
        this.$router.push('/')
      }
    }
  }
}
</script>

<style>

</style>