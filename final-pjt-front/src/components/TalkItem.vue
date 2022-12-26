<template>
  <div>
    <div id="reviewListItem">
      <div class="d-flex justify-content-between" id="reviewHead">
        <router-link
          :to="{ name: 'ProfileView', params: { username: item?.username } }"
          >{{ item?.username }}</router-link
        >
      </div>
      <div id="reviewContent">
        {{ item?.content }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TalkItem",
  props: {
    item: Object,
  },
  computed: {
    user() {
      return this.$store.getters.getUser;
    },
  },
};
</script>

<style>
@import "@/style/movie.css";
</style>
