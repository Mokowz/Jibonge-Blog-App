<template>
  <div class="container flex mx-auto">

    <form action="" @submit.prevent="postBlog" class="w-full flex items-center flex-col">
      <!-- Title and Tag -->
       <div class="w-full flex justify-between">
          <input type="text" v-model="title" placeholder="Title" class="mb-5 bg-white/10 px-4 rounded-sm py-3">
          <div>
            <select v-model="newTags" multiple size="1" class="bg-darkGrey/10 rounded-md px-8 py-3">
              <option value="" disabled>Add a Tag</option>
              <option :value="tag.id" v-for="tag in tags" :key="tag.name">{{ tag.name }}</option>
            </select>
          </div>
       </div>

       <!-- Content -->
        <div class="mt-6 w-full">
            <textarea rows="10" name="" id="" v-model="content" placeholder="Content" class="w-full mb-5 bg-white/10 px-4 rounded-sm py-3"></textarea>
        </div>

        <input type="submit" value="Post Blog" class="px-3 py-2 max-w-md cursor-pointer bg-yellow-500 font-semibold rounded-sm">
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import { apiBaseUrl } from '@/config';

export default {
  data() {
    return {
      title: '',
      tags: [],
      content: '',
      newTags: []
    }
  },

  created() {
    this.fetchTags()
  },

  watch: {
    newTags(newTag) {
      console.log(`New Tags: ${newTag}`)
    }
  },

  methods: {
    async postBlog() {
      console.log(`Tags: ${this.newTags}`)
      const response = await axios.post(`${apiBaseUrl}blogs/`, {
        title: this.title,
        tags: this.newTags,
        content: this.content,
      })

      if (response.status === 201) {
        this.$router.push('/')
      }
    },

    async fetchTags() {
      const response = await axios.get(`${apiBaseUrl}tags/`)

      if (response.status === 200) {
        this.tags = response.data
      }
    }
  }
}
</script>

<style>

</style>