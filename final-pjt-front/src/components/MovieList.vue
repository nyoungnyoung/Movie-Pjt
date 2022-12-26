<template>
  <div>
    <b-container class="bv-example-row">
      <MovieListItem
      v-for="movie in movies"
      :movie="movie"
      :key="movie.id"/>
    </b-container>
  </div>
</template>

<script>
import MovieListItem from "@/components/MovieListItem";

export default {
  name: "MovieList",
  props : {
    movies : Array
  },
  components: { 
    MovieListItem
    },
  methods : {
    getMovieList() {
        return this.$store.dispatch('getMovieList')
    }
  },
  created() {
    this.getMovieList()
  },
}
</script>

<style>
.container {
  display: flex;
  flex-wrap: wrap;
  justify-content:space-around;
  margin-top: 80px;
}
</style>
