<template>
  <div id="app">
    <header>
      <b-navbar
        class="navbar d-flex justify-content-between align-items-center"
      >
        <b-navbar-nav>
          <router-link :to="{ name: 'MainMovieView' }"
            ><img src="../../사진/Logo_row.png" alt="로고" class="logo"
          /></router-link>
          <b-nav-item>
            <router-link :to="{ name: 'MovieView' }" class="menuBar"
              >Movie</router-link
            >
          </b-nav-item>
          <b-nav-item>
            <router-link :to="{ name: 'RecommendGenreView' }" class="menuBar"
              >Recommend</router-link
            >
          </b-nav-item>
          <b-nav-item>
            <router-link :to="{ name: 'CommunityView' }" class="menuBar"
              >Community</router-link
            >
          </b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="right">
          <b-nav-form class="mt-1" style="margin-right: 10px" id="searchForm">
            <input
              placeholder="영화를 검색하세요!"
              v-model="search"
              type="text"
              v-on:keydown.enter.prevent="searchMovie"
              class="searchInput"
            />
            <b-avatar
              class="searchIcon"
              icon="search"
              @click="searchMovie"
            ></b-avatar>
            <!-- <b-button size="sm" class="my-2 my-sm-0" @click="searchMovie"
              >Search</b-button
            > -->
          </b-nav-form>

          <b-nav-item v-if="!isLogin">
            <router-link :to="{ name: 'LogInView' }" class="menuBar"
              >Login</router-link
            >
          </b-nav-item>
          <b-nav-item v-if="isLogin">
            <a @click="logOut" class="menuBar">LogOut</a>
          </b-nav-item>
          <b-nav-item v-if="!isLogin" style="margin-right: 10px">
            <router-link :to="{ name: 'SignUpView' }" class="menuBar"
              >SignUp</router-link
            >
          </b-nav-item>
          <b-nav-item v-if="isLogin" style="margin-right: 10px">
            <router-link
              :to="{
                name: 'ProfileView',
                params: { username: user?.username },
              }"
              class="menuBar"
              >MyPage</router-link
            >
          </b-nav-item>
          <router-link :to="{ name: 'MoviecupView' }"
            ><img src="../../사진/moviecup.png" alt="무비컵" class="movieCupicon" 
          /></router-link>
        </b-navbar-nav>
      </b-navbar>
    </header>

    <main>
      <router-view />
    </main>

    <footer></footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      search: null,
    };
  },
  computed: {
    isLogin() {
      if (this.$store.state.token) {
        return true;
      } else {
        return false;
      }
    },
    user() {
      if (this.isLogin == true) {
        return this.$store.getters.getUser;
      } else {
        return null;
      }
    },
    token() {
      if (this.isLogin == true) {
        return this.$store.state.token;
      } else {
        return null;
      }
    },
  },
  methods: {
    logOut() {
      this.$store.dispatch("logOut");
    },
    searchMovie() {
      this.$store.dispatch("searchMovieTitle", this.search);
      this.$store.dispatch("searchMovieOverview", this.search);
      this.$router.push({
        name: "SearchMovieView",
        params: { search: this.search },
      });
      this.search = "";
    },
  },
  watch: {
    token() {
      if (this.$store.state.token) {
        this.$store.dispatch("getUser");
      }
    },
  },
  created() {
    if (this.$store.state.token) {
      this.$store.dispatch("getUser");
    }
  },
};
</script>

<style>
@import "@/style/base.css";
</style>
