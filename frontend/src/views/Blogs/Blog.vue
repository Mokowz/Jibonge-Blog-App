<template>
  <div class="flex flex-col container mx-auto">
    <!-- Header -->
     <div class="text-center font-bold text-4xl border-b w-full border-darkGrey py-4">
        <h1>{{ blog.title }}</h1>
     </div>

    <!-- Rest -->
     <div class="flex mt-6  justify-between">
      <!-- Side Profile -->
       <div class="flex flex-col space-y-4 w-1/5">
        <!-- Author -->
        <div class="border-b border-darkGrey py-3 px-1">
          <h1 class="font-bold text-yellow-500 text-xl mb-2">Author</h1>
          <span>By {{ blog.author }}</span>
        </div>
        <div class="border-b border-darkGrey py-3 px-1">
          <h1 class="font-bold text-xl text-yellow-500 mb-2">Tags</h1>
          <span v-for="tag in blog.tags" :key="tag" class="mr-3">{{ tag }}</span>
        </div>
        <div class="border-b border-darkGrey py-3 px-1">
          <router-link to="/blogs" class="text-yellow-500"> << Back to Blogs</router-link>
        </div>
       </div>

       <!-- Content -->
       <div class="px-10 py-8 w-4/5">
          <p class="text-darkGrey">{{ blog.content }}</p>
       </div>

     </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      blog: {
        id: 1,
        title: 'Blog 1',
        content: "Asake's journey is one of inspiration and determination. Born in a small African village, she faced challenges with resilience and unwavering spirit. Despite limited resources and societal constraints, Asake remained steadfast in her pursuit of education. Through hard work and perseverance, she defied the odds and earned a scholarship to study abroad. Today, Asake stands as a beacon of hope, empowering others with her story of triumph over adversity. Her unwavering determination serves as a reminder that with passion and purpose, one can overcome any obstacle. Asake's journey inspires us to embrace our own potential and strive for greatness, no matter the circumstances.",
        author: 'Author 1',
        tags: ['tag1', 'tag2'],
        date: '2021-09-01',
      }
    }
  }
}
</script>

<style>

</style>