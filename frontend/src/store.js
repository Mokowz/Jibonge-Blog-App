import { createStore } from 'vuex';
import axios from 'axios';
import { useRoute } from 'vue-router';


const store = createStore({
  state: {
    user: null,
    token: null,
    loggedIn: false
  },

  mutations: {
    setUser(state, user) {
      state.user = user
    },

    setToken(state, token) {
      state.token = token
      state.loggedIn = true
      axios.defaults.headers.common["Authorization"] = `Bearer ${token}`
      localStorage.setItem('token', token)
    },

    clearAuth(state) {
      state.user = null
      state.token = null
      state.loggedIn = false
      localStorage.removeItem('token')
      axios.defaults.headers.common["Authorization"] = null
    }
  },

  actions: {
    initializeAuth({ commit }) {
      const token = localStorage.getItem('token')

      if (token) {
        commit('setToken', token)

        axios.get('')
        .then(response => {
          commit('setUser', response.data)
        })
        .catch(() => {
          commit('clearAuth')
        })
      }
    }
  }
})

export default store