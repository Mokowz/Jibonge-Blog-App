<template>
  <div class="flex w-full justify-between py-6 px-16 border-b border-darkGrey" v-for="blog in blogs" key="blog.id">
    <!-- Date side -->
     <span class="text-darkGrey">{{ blog.date }}</span>


    <!-- Content Side -->
    <div class="flex flex-col">
      <h1 class="text-2xl font-bold">{{ blog.title }}</h1>
      <div  class="flex flex-row space-x-2 uppercase">
        <h4 v-for="tag in blog.tags" :key="tag" class="text-yellow-500">{{ tag }}</h4>
      </div>
      <p class="text-dadrkGrey">{{ blog.content }}</p>

      <router-link to="/login" class="text-yellow-500 my-5 text-lg">Read More >> </router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      blogs: [
        {
          id: 1,
          title: 'Blog 1',
          content: 'Content nada',
          author: 'Author 1',
          tags: ['tag1', 'tag2'],
          date: '2021-09-01',
        },
        {
          id: 2,
          title: 'Blog 2',
          content: 'Content nada',
          author: 'Author 2',
          tags: ['tag1', 'tag2'],
          date: '2021-09-01',
        },

      ]
    }
  }
}
</script>

<style>

</style>