<template>
  <div>
    <carousel-3d  :controls-visible="true" :width="550" :height="780" :border="0" id="topMovieCarousel">
      <slide v-for="(movie, index) in movies" :index="index" :key="index">
        <TopMovieListItem :movie="movie" :key="movie.id"/>
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
import TopMovieListItem from "@/components/TopMovieListItem";
import { Carousel3d, Slide } from 'vue-carousel-3d'


export default {
  name: "TopMovieList",
  components: { 
    TopMovieListItem,
    Carousel3d,
    Slide
    },
    props:{
        movies : Array
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
@import '@/style/main.css';
</style>
