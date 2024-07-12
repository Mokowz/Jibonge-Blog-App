<template>
  <div class="flex flex-col container mx-auto px-4">
    <!-- Blog Header -->
     <div class="pb-5 flex justify-between items-center border-b border-darkGrey my-8">
      <div class="flex flex-col w-lg  space-y-3">
        <h1 class="text-4xl md:text-5xl font-bold">All Blogs</h1>
        <input type="search" v-model="searchInput" class="mb-5 max-w-sm bg-white/10 px-4 rounded-md py-3" placeholder="Search Blogs" @input="searchBlog">
      </div>

      <!-- Create new Blog -->
       <router-link v-if="loggedIn" to="/blog/new" class="px-3 py-2 bg-yellow-500 font-semibold rounded-sm">Write a Blog</router-link>
     </div>
     

     <!-- The Blogs -->
      <Blogs :search="searchValue" />

  </div>
</template>

<script>
import Blogs from '../../components/Blogs.vue';
import { mapState } from 'vuex';

export default {
  computed: {
    ...mapState(['loggedIn']),
  },
  components: {
    Blogs,
  },

  data() {
    return {
        searchValue: '',
        searchInput: '',
    }
  },

  methods: {
    searchBlog() {
      this.searchValue = this.searchInput;
    }
  },
}
</script>

<style>

</style>