<template>
  <div class="flex container mx-auto space-x-8">
    <div v-for="tag in tags" :key="tag" class="border border-darkGrey px-8 py-3 rounded-sm cursor-pointer">
      <router-link :to="{name:'tagList', params: {id: tag.id}}">{{ tag.name }}</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

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
      const response = await axios.get('http://54.144.151.102/api/v1/tags/')
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