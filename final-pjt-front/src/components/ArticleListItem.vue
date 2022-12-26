<template>
  <tr >
    <th scope="row">{{ article?.id }}</th>
    <td @click="toDetail">{{ article?.title }}</td>
    <td @click.prevent="toProfile">
      {{ user }}
    </td>
    <td>{{ createDate }}</td>
  </tr>
</template>

<script>
export default {
  name: "ArticleListItem",
  computed: {
    user() {
      return this.article?.username;
    },
    createDate() {
      return this.article?.created_at.substr(0, 10);
    },
  },
  props: {
    article: Object,
  },
  methods: {
    toDetail() {
      if(!this.$store.state.token){
        alert('로그인하세요')
        this.$router.push({ name: "LogInView" }) 
      }
      else{
      this.$router.push({
        name: "ArticleDetailView",
        params: { article_id: this.article?.id },
      });}
    },
    toProfile(){
      this.$router.push({ name: 'ProfileView', params: { username: this.user } })
    }
  },
};
</script>

<style>
</style>