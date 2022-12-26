<template>
  <div class="container">
    <div>
      <h1>추천영화</h1>
    </div>
    <div>
      <hr />
      <h4 style="margin-top: 30px">
        당신이 가장 좋아하는 장르는 {{ max_genre_like }}
      </h4>
      <div style="margin-top: -50px">
        <MovieList :movies="first_recommend" />
      </div>
      <hr />
      <h4 style="margin-top: 30px">다음으로 좋아하는 장르는 {{ second_genre_like }}</h4>
      <div style="margin-top: -50px">
        <MovieList :movies="second_recommend" />
      </div>
    </div>
  </div>
</template>

<script>
import MovieList from "@/components/MovieList.vue";
import axios from "axios";
const API_URL = "http://localhost:8000";

export default {
  name: "RecommendGenreView",
  components: {
    MovieList,
  },
  data() {
    return {
      max_genre_like: null,
      second_genre_like: null,
      first_recommend: null,
      second_recommend: null,
    };
  },
  methods: {
    getRecommendGenre() {
      axios({
        method: "get",
        url: `${API_URL}/movies/recommend/genre/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          this.max_genre_like = response.data["max_genre_like"];
          this.second_genre_like = response.data["second_genre_like"];
          this.first_recommend = response.data["first_recommend"];
          this.second_recommend = response.data["second_recommend"];
        })
        .catch(() => {
          alert('영화에 좋아요를 해주세요!')
          this.$router.go(-1)
        });
    },
    check() {
      if (this.user.like_movies.length == 0) {
        alert("영화에 좋아요를 해주세요!");
      }
    },
  },
  created() {
    // this.check();
    this.getRecommendGenre();
  },
};
</script>

<style>
.container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-top: 80px;
}
</style>
