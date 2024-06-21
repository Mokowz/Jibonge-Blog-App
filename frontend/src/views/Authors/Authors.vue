<template>
  <div class="flex container mx-auto">
    <div v-for="author in authors" :key="author">
        <span  class="mr-6 px-6 py-3 border rounded-sm border-darkGrey">{{ author }}</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      authors: [
        'author1',
        'author2',
        'author3',
      ]
    }
  }
}
</script>

<style>

</style>