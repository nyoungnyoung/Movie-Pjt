<template>
  <div>
    <b-row>
      <b-col @click="toDetail">
        <img
          :src="`https://image.tmdb.org/t/p/w300/${movie?.poster_path}`"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem"
          class="mb-2"
          id="card"
        />
      
        <!-- <b-card-text class="overview">
          {{ movie?.overview }}
        </b-card-text>
        <b-button href="#" variant="secondary">Detail</b-button> -->
        <!-- </img> -->
        <p @click.stop="likeMovie">
          <span>{{ like }}</span> {{ like_count }}
        </p>
        <!-- <b-button href="#" variant="secondary">Detail</b-button> -->
        <!-- </b-card> -->
      </b-col>
    </b-row>
  </div>
</template>

<script>
import _ from "lodash";
import axios from "axios";
const API_URL = "http://localhost:8000";

export default {
  name: "MovieListItem",
  props: {
    movie: Object,
  },
  data() {
    return {
      is_like: false,
      like_count: _.size(this.movie?.like_users),
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
    get_is_like() {
      if (this.movie?.like_users.includes(this.user.pk)) {
        this.is_like = true;
      } else {
        this.is_like = false;
      }
    },
    toDetail() {
      this.$router.push({
        name: "MovieDetailView",
        params: { tmdb_id: this.movie?.tmdb_id,movie_id :this.movie?.id },
      });
    },
    likeMovie() {
      if (!this.$store.state.token) {
        alert("로그인하세요");
        return;
      } else {
        axios({
          method: "post",
          url: `${API_URL}/movies/${this.movie.id}/like/`,
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
    if (this.$store.state.token) {
      this.get_is_like();
    }
  },
};
</script>

<style>
@import "@/style/movie.css";
</style>
