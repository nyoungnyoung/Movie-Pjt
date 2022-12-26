<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
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
import axios from "axios";
const API_URL = "http://localhost:8000";

export default {
  name: "ArticleCreateView",
  data() {
    return {
      title: null,
      content: null,
      board : 1,
    };
  },
  methods: {
    createArticle() {
      if (!this.title) {
        alert("제목을 입력해주세요");
        return;
      } else if (!this.content) {
        alert("내용을 입력해주세요");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/community/create/`,
        data: {
          title: this.title,
          content: this.content,
          board_number : this.board,
        },
        headers : {
          Authorization : `Token ${this.$store.state.token}`
        }
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
