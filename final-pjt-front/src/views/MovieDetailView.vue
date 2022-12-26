<template>
  <div>
    <div class="d-flex" id="infoContainer">
      <!-- 왼쪽 -->
      <div class="d-flex flex-column" id="leftcards">
        <div class="leftFirstCard">
          <img :src="poster_path" alt="image" class="movieImage" />
        </div>
        <b-card header="TAGS" id="movieGenres">
          <span v-for="(genre, idx) in genres" :key="idx">
            {{ genre }}
          </span>
        </b-card>
      </div>

      <!-- 오른쪽 -->
      <div class="d-flex flex-column" id="rightcards">
        <iframe
          :src="video_url"
          autoplay
          muted
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          class="movieVideo"
        ></iframe>
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

    <div id="bottomcards">
      <div class="detailReview">
        <b-avatar
          v-b-toggle.collapseReview
          id="commentBtn"
          icon="chat-square-dots-fill"
        ></b-avatar>
        <b-collapse visible id="collapseReview" class="mt-2">
          <b-card id="reviewCard">
            <h5>리뷰</h5>
            <ReviewList :movie="movie" :movie_id="Number(movie_id)" />
          </b-card>
        </b-collapse>
      </div>
    </div>
  </div>
</template>

<script>
const API_URL = "http://localhost:8000";
import axios from "axios";
import _ from "lodash";
import ReviewList from "@/components/ReviewList.vue";

export default {
  name: "MovieDetailView",
  components: {
    ReviewList,
  },
  data() {
    return {
      movie_id: this.$route.params.movie_id,
      tmdb_id: this.$route.params.tmdb_id,
      movie: null,
      genres: null,
      is_like: false,
      like_count: null,
      poster_path: null,
      video_url: null,
    };
  },
  computed: {
    user() {
      return this.$store.getters.getUser;
    },
    like() {
      return this.is_like ? "❤️" : "🤍";
    },
  },
  methods: {
    getMovie() {
      const API_KEY = "487b617acdcef17f4628cd13e62a835c";
      const MOVIE_URL = `https://api.themoviedb.org/3/movie/${this.tmdb_id}?api_key=${API_KEY}&language=ko`;
      axios({
        method: "get",
        url: MOVIE_URL,
      })
        .then((response) => {
          this.movie = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getMovieInfo() {
      axios({
        method: "get",
        url: `${API_URL}/movies/${this.movie_id}/`,
      })
        .then((response) => {
          const user = this.$store.getters.getUser
          const movie = response.data;
          this.like_count = _.size(movie?.like_users);
          this.poster_path =
            "https://image.tmdb.org/t/p/w500" + movie.poster_path;
          this.video_url = movie.video_url + "?autoplay=1&loop=1";
          this.genres = movie.genres;
          if (this.$store.state.token) {
            if (movie.like_users.includes(user.pk)) {
              console.log('dd')
              this.is_like = true;
            } else {
              this.is_like = false;
            }
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    likeMovie() {
      if (!this.$store.state.token) {
        alert("로그인하세요");
        return;
      } else {
        axios({
          method: "post",
          url: `${API_URL}/movies/${this.movie_id}/like/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            this.is_like = res.data["like"];
            this.like_count = res.data["like_count"];
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
  created() {
    this.getMovie();
    this.getMovieInfo();
  },
};
</script>

<style>
@import "@/style/movie.css";
</style>
