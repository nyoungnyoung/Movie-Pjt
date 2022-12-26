import axios from "axios"
import Vue from "vue"
import Vuex from "vuex"
import router from '../router'
import createPersistedState from 'vuex-persistedstate'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(Vuex);

const API_URL = "http://localhost:8000"

export default new Vuex.Store({
  state: {
    movies: [],
    movie: null,
    random_movie: null,
    articles: [],
    article: null,
    token: null,
    user: null,
    //검색
    search_keyword:null,
    title_movies:null,
    overview_movies : null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    getMovies(state) {
      return state.movies
    },
    getMovie(state) {
      return state.movie
    },
    getArticles(state) {
      return state.articles
    },
    getUser(state){
      return state.user
    },
    getTitleMovie(state){
      return state.title_movies
    },
    getOverviewMovie(state){
      return state.overview_movies
    }
    
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      state.isLogin = true
      router.push({ name: "MainMovieView"})
    },
    LOGIN_USER(state, user) {
      state.token = user
    },
    LOG_OUT(state) {
      state.token = null
      state.user = null
      state.isLogin = false
      router.push({ name: "MainMovieView"})
    },
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_MOVIE(state, movie) {
      state.movie = movie
    },
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    GET_USER(state,user){
      state.user = user
    },
    //검색
    GET_SEARCH_TITLE(state,payload){
      state.title_movies = payload.movies
      state.search_keyword = payload.search
    },
    GET_SEARCH_OVERVIEW(state,payload){
      state.overview_movies = payload.movies
      state.search_keyword = payload.search
    }

  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then(response => {
          context.commit('SAVE_TOKEN', response.data.key)
        })
        .catch(error => {
          console.log(error)
        })
    },
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then(response => {
          context.commit('SAVE_TOKEN', response.data.key)
        })
        .catch(error => {
          console.log(error)
        })
    },
    logOut({commit}) {
      commit('LOG_OUT')
    },
    ///////////////나중에삭제
    getMovieList(context) {
      axios({
        method: "get",
        url: `${API_URL}/movies/`,
      })
        .then((response) => {
          context.commit("GET_MOVIES", response.data)
        })
        .catch((error) => {
          console.log(error)
        });
    },
    getRandomMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/movies/random/`,
      })
        .then((response) => {
          context.commit("GET_MOVIE", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    ////
    getArticles(context, board_number) {
      axios({
        method: 'get',
        url: `${API_URL}/community/${board_number}/`,
      }).then((response) => {
        context.commit('GET_ARTICLES', response.data)
      }).catch((error) => {
        console.log(error)
      })
    },
    getUser(context){
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers : {
          Authorization : `Token ${context.state.token}`
        }
      }).then((response) => {
        context.commit('GET_USER',response.data)
      }).catch((error) => {
        console.log(error)
      })
    },
    searchMovieTitle(context,search){
      axios({
        method: 'get',
        url: `${API_URL}/movies/search/title/`,
        params: {
          search : search
        }
      }).then((response) => {
        const payload = {
          movies : response.data,
          search : search
        }
        context.commit('GET_SEARCH_TITLE',payload)
      }).catch((error) => {
        console.log(error)
      })
    },
    searchMovieOverview(context,search){
      axios({
        method: 'get',
        url: `${API_URL}/movies/search/overview/`,
        params: {
          search : search
        }
      }).then((response) => {
        const payload = {
          movies : response.data,
          search : search
        }
        context.commit('GET_SEARCH_OVERVIEW',payload)
      }).catch((error) => {
        console.log(error)
      })
    },

  },
  modules: {
  },
  // 토큰 로컬스토리지에 저장
  plugins: [
    createPersistedState(),
  ]
})
