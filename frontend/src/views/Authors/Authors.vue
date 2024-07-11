<template>
  <div v-if="construction" class="grid md:grid-cols-3 grid-cols-2 gap-4 container mx-auto px-4">
    <div v-for="author in authors" :key="author.id" class="md:mr-6 px-6 py-3 flex items-center justify-center border rounded-sm border-darkGrey">
        <router-link :to="{name: 'authorBlogs', params: {id: author.id}}">{{ author.user.first_name }} {{ author.user.last_name }}</router-link>
    </div>
  </div>
  <div v-else class="flex container flex-wrap max-w-md gap-x-4 gap-y-10 mx-auto px-4">
    <h1 class="text-4xl font-semibold">Under Construction</h1>
    <p>This page is currently undergoing scheduled maintenance. We will be back shortly. Thank you for your patience.</p>
    <router-link to="/" class="text-yellow-500 underline">Go Back to The Home Page</router-link>
  </div>
</template>

<script>
import axios from 'axios';
import { apiBaseUrl } from '@/config';

export default {
  data() {
    return {
      authors: [],
      construction: true
    }
  },

  created() {
    this.fetchAuthors()
  },

  methods: {
    async fetchAuthors() {
      const response = await axios.get(`${apiBaseUrl}authors/`)
                      .then((response) => {
                        this.authors = response.data;
                      })
      console.log(`Authors: ${this.authors}`)
      // for (let author in this.authors) {
      //   console.log(`Author: ${author.bio}`)
      // }
    }
  }
}
</script>

<style>

</style>