<template>
  <div>
    <h1>{{profileUser.username}}님이 좋아하는 영화</h1>
    <router-link
              :to="{
                name: 'ProfileView',
                params: { username: profileUser?.username },
              }"
              >{{profileUser.username}}님의 프로필로 되돌아가기</router-link
            >
    <MovieList :movies="like_movies"/>
  </div>
</template>

<script>
const API_URL = "http://localhost:8000";
import axios from "axios";

import MovieList from "@/components/MovieList.vue";
export default {
  name: "LikeMovieView",
  components: {
    MovieList,
  },
  data() {
    return {
      username: this.$route.params.username,
      profileUser : null,
        like_movies : null,
    };
  },
  methods: {
    getUserInfo() {
      axios({
        method: "get",
        url: `${API_URL}/accountsinfo/${this.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          this.profileUser = response.data;
          this.getFollowInfo()
        })
        .catch(() => {
        });
    },
    getFollowInfo() {
      axios({
        method: "get",
        url: `${API_URL}/accountsinfo/${this.username}/info/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          this.like_movies = response.data["like_movies"];
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created(){
    this.getUserInfo()
  }
};
</script>

<style>
</style>