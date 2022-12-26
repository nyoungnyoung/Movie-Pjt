<template>
  <!-- <div> -->
    <!-- <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img :src="`https://image.tmdb.org/t/p/w300/${movie?.poster_path}`" class="carouseImg d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="dog.png" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="bird.png" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div> -->
    <img :src="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`" class="carouselImg" @click="toDetail">

    <!-- <b-row>
      <b-col @click="toDetail">
        <b-card
          :title="`${movie?.title}`"
          :img-src="`https://image.tmdb.org/t/p/w300/${movie?.poster_path}`"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem"
          class="mb-2"
        >
          <b-card-text class="overview">
            {{ movie?.overview }}
          </b-card-text>
          <b-button href="#" variant="secondary">Detail</b-button>
        </b-card>
      </b-col>
    </b-row> -->
  <!-- </div> -->
</template>

<script>
export default {
  name: "TopMovieListItem",
  props: {
    movie: Object,
  },
  methods: {
    toDetail() {
      this.$router.push({
        name: "TopMovieDetailView",
        params: { movie_id: this.movie.id },
      });
    },
  },
};
</script>

<style>
@import "@/style/main.css";
</style>
