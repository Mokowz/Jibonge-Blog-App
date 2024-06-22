<template>
  <div class="flex container mx-auto">
    <div v-for="author in authors" :key="author">
        <span  class="mr-6 px-6 py-3 border rounded-sm border-darkGrey">{{ author.bio }}</span>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

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
      const response = await axios.get('http://54.144.151.102/api/v1/authors/')
                      .then((response) => {
                        this.authors = response.data;
                      })
    }
  }
}
</script>

<style>

</style>