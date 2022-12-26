<template>
  <div>
    <br />
    <br />
    <br />
    <h2>"{{ search }}" 검색 결과 입니다</h2>
    <h3>제목 검색 결과</h3>
    <MovieList :movies="title_movies" />
    <hr />
    <div>
      <br />
      <br />
      <br />
      <h3>혹시 이것을 찾으시나요..? overview 검색 결과</h3>
      <MovieList :movies="overview_movies" />
    </div>
  </div>
</template>

<script>
import MovieList from "@/components/MovieList.vue";
export default {
  name: "SearchMovieView",
  components: {
    MovieList,
  },
  data() {
    return {
      noTitle: false,
      noOverview: false,
    };
  },
  computed: {
    search() {
      return this.$store.state.search_keyword;
    },
    title_movies() {
      return this.$store.getters.getTitleMovie;
    },
    overview_movies() {
      return this.$store.getters.getOverviewMovie;
    },
  },
};
</script>

<style></style>
