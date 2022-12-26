<template>
  <div>
    <b-row>
      <b-col>
        <img
          :src="`https://image.tmdb.org/t/p/w300/${movie?.poster_path}`"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem"
          class="mb-2"
          id="card"
        />
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: "MoviecupListItem",
  props: {
    movie: Object,
  },
};
</script>

<style>
@import "@/style/movie.css";
</style>
