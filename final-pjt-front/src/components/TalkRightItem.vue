<template>
  <div>
    <div id="talkListItemRight">
      <div class="d-flex justify-content-between">
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
  name: "TalkLeftItem",
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
