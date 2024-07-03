<template>
  <div class="flex flex-col-reverse md:flex-row w-full justify-between py-6 md:px-16 border-b border-darkGrey" v-for="blog in blogs" :key="blog.id">
    <!-- Date side -->
     <span class="text-darkGrey">{{ blog.created_at }}</span>


    <!-- Content Side -->
    <div class="flex flex-col md:w-3/6">
      <h1 class="text-2xl font-bold">{{ blog.title }}</h1>
      <div  class="flex flex-row space-x-2 uppercase">
        <h4 v-for="tag in blog.tags" :key="tag" class="text-yellow-500">{{ tag.name }}</h4>
      </div>
      <p class="text-darkGrey my-2">{{ blog.content.slice(0,200) }}...</p>

      <router-link :to="{name: 'blog', params: {id: blog.id}}" class="text-yellow-500 my-5 text-lg">Read More >> </router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { apiBaseUrl } from '../config';

export default {
  props: ['search'],
  data() {
    return {
      blogs: []

    }
  },

  methods: {
    async fetchBlogs() {
      const response = await axios.get(`${apiBaseUrl}blogs/?search=${this.search}`)
        .then((response) => {
          this.blogs = response.data;
      })
    }
  },

  watch: {
    search(newValue, oldValue) {
      this.fetchBlogs();
    }
  },

  created() {
    this.fetchBlogs();
  },
}
</script>

<style>

</style>