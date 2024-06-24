<template>
  <div class="flex container mx-auto space-x-8 px-4">
    <div v-for="tag in tags" :key="tag" class="border border-darkGrey px-8 py-3 rounded-sm cursor-pointer">
      <router-link :to="{name:'tagList', params: {id: tag.id}}">
        {{ tag.name }}
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { apiBaseUrl } from '@/config';

export default {
  data() {
    return {
      tags: []
    }
  },

  created() {
    this.fetchTags()
  },

  methods: {
    async fetchTags() {
      const response = await axios.get(`${apiBaseUrl}tags/`)
                      .then((response) => {
                        this.tags = response.data;
                      }
      )
    }
  }, 
}
</script>

<style>

</style>