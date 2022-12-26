<template>
  <div>
    <h1>Detail</h1>
    <div class="d-flex" id="infoContainer">
      <!-- 왼쪽 -->
      <div class="d-flex flex-column" id="leftcards">
        <div class="leftFirstCard">
          <img
      :src="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`"
      alt=""
    />
        </div>
      </div>

      <!-- 오른쪽 -->
      <div class="d-flex flex-column" id="rightcards">
        <b-card id="detailInfo">
          <h3>{{ movie?.title }}</h3>
          <p @click.stop="likeMovie">
            <span>{{ like }}</span> {{ like_count }}
          </p>
          <p>{{ movie?.overview }}</p>
          <p>평점 : {{ movie?.vote_average }}</p>
          <p>개봉일 : {{ movie?.release_date }}</p>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "TopMovieDetailView",
  data() {
    return {
      movie : null
    };
  },
  methods: {
    toDetail() {
      const API_KEY = "487b617acdcef17f4628cd13e62a835c";
      const MOVIE_URL = `https://api.themoviedb.org/3/movie/${this.$route.params.movie_id}?api_key=${API_KEY}&language=ko`;
      axios({
        method: "get",
        url: `${MOVIE_URL}`,
      })
        .then((response) => {
          this.movie = response.data
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created(){
    this.toDetail()
  }
};
</script>

<style>
</style>