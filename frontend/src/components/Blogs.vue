<template>
  <div class="flex w-full justify-between py-6 px-16 border-b border-darkGrey" v-for="blog in blogs" :key="blog.id">
    <!-- Date side -->
     <span class="text-darkGrey">{{ blog.created_at }}</span>


    <!-- Content Side -->
    <div class="flex flex-col w-3/6">
      <h1 class="text-2xl font-bold">{{ blog.title }}</h1>
      <div  class="flex flex-row space-x-2 uppercase">
        <h4 v-for="tag in blog.tags" :key="tag" class="text-yellow-500">{{ tag }}</h4>
      </div>
      <p class="text-darkGrey my-2">{{ blog.content.slice(0,200) }}...</p>

      <router-link to="/blog/1" class="text-yellow-500 my-5 text-lg">Read More >> </router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
    //   blogs: [
    //     {
    //       id: 1,
    //       title: 'Blog 1',
    //       content: "Asake's journey is one of inspiration and determination. Born in a small African village, she faced challenges with resilience and unwavering spirit. Despite limited resources and societal constraints, Asake remained steadfast in her pursuit of education. Through hard work and perseverance, she defied the odds and earned a scholarship to study abroad. Today, Asake stands as a beacon of hope, empowering others with her story of triumph over adversity. Her unwavering determination serves as a reminder that with passion and purpose, one can overcome any obstacle. Asake's journey inspires us to embrace our own potential and strive for greatness, no matter the circumstances.",
    //       author: 'Author 1',
    //       tags: ['tag1', 'tag2'],
    //       date: '2021-09-01',
    //     },
    //     {
    //       id: 2,
    //       title: 'Blog 2',
    //       content: 'Content nada',
    //       author: 'Author 2',
    //       tags: ['tag1', 'tag2'],
    //       date: '2021-09-01',
    //     },

    //   ]
    blogs: []

    }
  },

  beforeMount() {
    axios.get('http://54.144.151.102/api/v1/blogs/')
    .then((response) => {
      this.blogs = response.data;
    })
  },
}
</script>

<style>

</style>