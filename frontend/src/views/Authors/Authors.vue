<template>
  <div class="flex container mx-auto px-4">
    <div v-for="author in authors" :key="author">
        <router-link :to="{name: 'authorBlogs', params: {id: author.id}}"  class="mr-6 px-6 py-3 border rounded-sm border-darkGrey">{{ author.bio }}</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { apiBaseUrl } from '@/config';

export default {
  data() {
    return {
      authors: []
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
    }
  }
}
</script>

<style>

</style>