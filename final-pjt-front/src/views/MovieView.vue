<template>
  <div class="container">
    <form method="get" action="form-action.html">
      <h3>보고싶은 영화 장르를 선택하세요!</h3>
        <input type="checkbox" id="check_all" @click="selectAll()" />
        <b>Select All</b>
        <label  @click="setGenres" v-for="(genre, idx) in all_genres" :key="idx">
          <input
          style="margin: 5px"
          type="checkbox"
          name="genre"
          :value="genre"
          />{{ genre }}</label
          >
          <input type="reset" value="reset" />
        </form>
    <div>
      <MovieList :movies="movies" />
    </div>
  </div>
</template>

<script>
import MovieList from "@/components/MovieList.vue";
import axios from "axios";
const API_URL = "http://localhost:8000";

export default {
  name: "MovieView",
  components: {
    MovieList,
  },
  data() {
    return {
      all_genres: [
        "액션",
        "모험",
        "애니메이션",
        "코미디",
        "다큐멘터리",
        "드라마",
        "가족",
        "판타지",
        "역사",
        "공포",
        "로맨스",
        "SF",
        "스릴러",
        "전쟁",
      ],
      movies: null,
      all_movies: null,
      want_genre: null,
    };
  },
  methods: {
    getMovies() {
      axios({
        method: "get",
        url: `${API_URL}/movies/`,
      })
        .then((response) => {
          this.movies = response.data;
          this.all_movies = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    plusGenre(genre) {
      this.want_genre.append(genre);
    },
    minusGenre(genre) {
      const idx = this.want_genre.indexOf(genre);
      if (idx > -1) {
        this.want_genre.splice(idx, 1);
      }
    },
    setGenres() {
      const query = 'input[name="genre"]:checked';
      const selectedEls = document.querySelectorAll(query);
      let result = [];
      selectedEls.forEach((el) => {
        result.push(el.value);
      });
      this.want_genre = result;
    },
    selectAll() {
      const checkboxes = document.querySelectorAll('input[type="checkbox"]');
      const all = document.querySelector('#check_all')
      checkboxes.forEach((checkbox) => {
        checkbox.checked = all.checked;
      });
    },
    getGenreMovies() {
      let temp = [];
      this.all_movies.forEach((movie) => {
        movie.genres.forEach((genre) => {
          if (this.want_genre.includes(genre)) {
            if (!temp.includes(movie)) temp.push(movie);
          }
        });
      });
      this.movies = temp;
    },
  },
  created() {
    this.getMovies();
  },
  watch: {
    want_genre() {
      this.getGenreMovies();
    },
  },
};
</script>

<style>
input, progress {
  accent-color: rgb(255, 183, 181);
}
input[type=reset]{
margin-top:3%;
  margin-left:45%;
  display: block;
  width: 100px;
  height:30px;
  background-color: rgb(255, 183, 181);
  border: none;
  border-radius: 5px;
}
</style>