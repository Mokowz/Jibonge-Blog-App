<template class="bg-slate-900">
  <div>
    <Navbar />
    <router-view/>
    <Footer />
  </div>
</template>

<script>
import Footer from './components/Footer.vue'
import Navbar from './components/Navbar.vue'

export default {
  components: {
    Navbar,
    Footer,
  }
}

</script>

<style>

</style>
