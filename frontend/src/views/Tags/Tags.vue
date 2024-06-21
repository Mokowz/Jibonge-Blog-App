<template>
  <div class="flex container mx-auto space-x-8">
    <div v-for="tag in tags" :key="tag" class="border border-darkGrey px-6 py-3 rounded-md cursor-pointer">
      <span>{{ tag }}</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tags: [
        'hello',
        'tag2',
        'tags3',
      ]
    }
  }
}
</script>

<style>

</style>