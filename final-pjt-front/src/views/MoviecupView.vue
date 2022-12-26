<template>
  <div>
    <img src="../../../사진/moviecup.png" />
    <h3>
      {{ user?.username }}님의 이전 영화월드컵 우승은... {{ originmoviecup.title }}
    </h3>
    <hr />
    <div>
      <button class="n_btn" @click="click16" v-if="!start">16강</button>
      <button class="n_btn" @click="click32" v-if="!start">32강</button>
      <button
        @click="restart"
        class="n_btn"
        v-if="start"
        style="margin-bottom: 20px"
      >
        다시하기
      </button>
    </div>
    <div v-if="start" style="display: flex">
      <div @click="select1" style="margin: auto">
        <h3>
          {{ movie1.title }}
        </h3>
        <MoviecupListItem :movie="movie1" />
      </div>
      <div @click="select2" style="margin: auto">
        <h3>
          {{ movie2.title }}
        </h3>
        <MoviecupListItem :movie="movie2" />
      </div>
    </div>
  </div>
</template>

<script>
const API_URL = "http://localhost:8000";
import axios from "axios";
import MoviecupListItem from "@/components/MoviecupListItem.vue";

export default {
  name: "MoviecupView",
  components: {
    MoviecupListItem,
  },
  data() {
    return {
      movies: null,
      movie1: null,
      movie2: null,
      mymoviecup: null,
      num: null,
      start: false,
      originmoviecup: "정보가 없습니다.",
    };
  },
  computed: {
    user() {
      return this.$store.getters.getUser;
    },
  },
  methods: {
    click16() {
      this.num = 16;
      this.getMovies();
      this.start = true;
    },
    click32() {
      this.num = 32;
      this.getMovies();
      this.start = true;
    },
    restart() {
      this.$router.go(this.$router.currentRoute);
    },
    getMoviecupInfo() {
      axios({
        method: "get",
        url: `${API_URL}/accountsinfo/moviecup/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          this.originmoviecup = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getMovies() {
      //랜덤 영화 가져오기
      axios({
        method: "get",
        url: `${API_URL}/movies/candidate/`,
        params: {
          num: this.num,
        },
      })
        .then((response) => {
          this.movies = response.data;
          this.movie1 = this.movies.shift();
          this.movie2 = this.movies.shift();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getCandidate() {
      this.movie1 = this.movies.shift();
      this.movie2 = this.movies.shift();
    },
    select1() {
      this.movies.push(this.movie1);
      this.my_moviecup = this.movie1;
      this.getCandidate();
      if (!this.movie1 || !this.movie2) {
        this.setMoviecup();
      }
    },
    select2() {
      this.movies.push(this.movie2);
      this.my_moviecup = this.movie2;
      this.getCandidate();
      if (!this.movie1 || !this.movie2) {
        this.setMoviecup();
      }
    },
    setMoviecup() {
      axios({
        method: "post",
        url: `${API_URL}/movies/moviecup/`,
        data: {
          movie_id: this.my_moviecup.id,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          alert("무비컵 우승 영화 디테일로 이동합니다!");
          this.$router.push({
            name: "MovieDetailView",
            params: {
              movie_id: this.my_moviecup.id,
              tmdb_id: this.my_moviecup.tmdb_id,
            },
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    myMoviecup() {
      axios({
        method: "get",
        url: `${API_URL}/movies/moviecup/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          this.originmoviecup = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.myMoviecup();
  },
};
</script>

<style>
.n_btn {
  margin-top: 1%;
  justify-content: center;
  margin-left: 45%;
  display: block;
  width: 130px;
  height: 40px;
  background-color: rgb(255, 183, 181);
  border: none;
  border-radius: 5px;
}
</style>
