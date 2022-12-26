<template>
  <div>
    <h1>게시글 수정</h1>
    ---기존 작성글---
    <ArticleListItem
      :article="article"
      :key="article.id"
    />
    <form @submit.prevent="updateArticle">
      <select v-model="board">
        <option value="1">자유게시판</option>
        <option value="2">영화추천</option>
        <option value="3">극장정보</option>
      </select>
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title" /><br />
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea
      ><br />
      <input type="submit" id="submit" />
    </form>
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'
import axios from "axios"
const API_URL = "http://localhost:8000"

export default {
  name: "ArticleUpdateView",
  components : {
    ArticleListItem
  },
  data() {
    return {
      title: this.$route.params.article.title,
      content: this.$route.params.article.content,
      board : this.$route.params.article.board_number,
    };
  },
  computed : {
    article(){
        return this.$route.params.article
    },
  },
  methods: {
    updateArticle() {
      if (!this.title) {
        alert("제목을 입력해주세요");
        return;
      } else if (!this.content) {
        alert("내용을 입력해주세요");
        return;
      }
      axios({
        method: "put",
        url: `${API_URL}/community/article/${this.$route.params.article.id}/`,
        data: {
          title: this.title,
          content: this.content,
          board_number : this.board
        },
      })
        .then(() => {
          this.$router.push({ name: "CommunityView" });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
</style>
