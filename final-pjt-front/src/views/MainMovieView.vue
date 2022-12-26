<template>
  <div>
    <br />
    <div id="top20List">
      <h1>TOP20</h1>
      <TopMovieList :movies="topMovies" />
    </div>
    <div id="userRecommendList">
      <h3>랜덤 영화 추천</h3>
      <vueper-slides
        class="no-shadow"
        :visible-slides="3"
        :gap="3"
        :slide-ratio="1 / 4"
        :infinite="true"
        fixed-height="450px"
        arrows-outside
        :bullets="false"
        :breakpoints="{
          600: { visibleSlides: 1 },
          850: { visibleSlides: 2 },
          1400: { visibleSlides: 3 },
          1650: { visibleSlides: 4 },
          2000: { visibleSlides: 5 },
        }"
      >
        <vueper-slide
          v-for="(movie, index) in random_movies"
          :key="index"
          :image="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`"
          
        >
        </vueper-slide>
      </vueper-slides>
    </div>
    <div id="userRecommendList">
      <h3>인기있는 애니메이션 추천</h3>
      <vueper-slides
        class="no-shadow"
        :visible-slides="3"
        :gap="3"
        :slide-ratio="1 / 4"
        fixed-height="450px"
        arrows-outside
        :bullets="false"
        :breakpoints="{
          600: { visibleSlides: 1 },
          850: { visibleSlides: 2 },
          1400: { visibleSlides: 3 },
          1650: { visibleSlides: 4 },
          2000: { visibleSlides: 5 },
        }"
      >
        <vueper-slide
          v-for="(movie, index) in ani_movies"
          :key="index"
          :image="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`">
        </vueper-slide>
      </vueper-slides>
    </div>
    <div id="userRecommendList">
      <h3>인기있는 판타지 영화 추천</h3>
      <vueper-slides
        class="no-shadow"
        :visible-slides="3"
        slide-multiple
        :gap="3"
        :slide-ratio="1 / 4"
        fixed-height="450px"
        arrows-outside
        :bullets="false"
        :breakpoints="{
          600: { visibleSlides: 1, slideMultiple: 1 },
          850: { visibleSlides: 2, slideMultiple: 1 },
          1400: { visibleSlides: 3, slideMultiple: 1 },
          1650: { visibleSlides: 4, slideMultiple: 1 },
          2000: { visibleSlides: 5, slideMultiple: 1 },
        }">
        <vueper-slide
          v-for="(movie, index) in fantasy_movies"
          :key="index"
          :image="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`"
        >
        </vueper-slide>
      </vueper-slides>
    </div>
  </div>
</template>

<script>
const API_URL = "http://localhost:8000";
import TopMovieList from "@/components/TopMovieList";
import axios from "axios";
import { VueperSlides, VueperSlide } from "vueperslides";
import "vueperslides/dist/vueperslides.css";

export default {
  name: "MainMovieView",
  data() {
    return {
      topMovies: null,
      random_movies:null,
      ani_movies:null,
      fantasy_movies:null,
    };
  },
  computed: {
    loginUser() {
      return this.$store.getters.getUser.username;
    },
  },
  components: {
    TopMovieList,
    VueperSlides,
    VueperSlide,
  },
  methods: {
    getTopMovies() {
      const API_KEY = "487b617acdcef17f4628cd13e62a835c";
      const MOVIE_URL = `https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}&language=ko`;
      axios({
        method: "get",
        url: `${MOVIE_URL}`,
      })
        .then((response) => {
          this.topMovies = response.data.results;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getRandomMovies() {
      axios({
        method: "get",
        url: `${API_URL}/movies/random/`,
      })
        .then((response) => {
          this.random_movies = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getAniMovies() {
      const genre_id = 16
      axios({
        method: "get",
        url: `${API_URL}/movies/recommend/genre/${genre_id}/`,

      }).then((response) => {
        this.ani_movies = response.data['movies']
      }).catch((error) => {
        console.log(error)
      })
    },
    getFantasyMovies() {
      const genre_id = 14
      axios({
        method: 'get',
        url: `${API_URL}/movies/recommend/genre/${genre_id}/`,

      }).then((response) => {
        this.fantasy_movies = response.data['movies']
      }).catch((error) => {
        console.log(error)
      })
        .then((response) => {
          this.romance_movies = response.data["movies"];
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getTopMovies();
    this.getRandomMovies();
    this.getAniMovies();
    this.getFantasyMovies();
  },
};
</script>

<style>
@import "@/style/main.css";
</style>
