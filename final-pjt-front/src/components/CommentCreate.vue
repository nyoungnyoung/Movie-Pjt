<template>
  <div>
    <form @submit.prevent="createComment" id="commentForm" class="d-flex justify-content-between">
      <textarea 
      placeholder = '댓글을 입력하세요'
      id="content" cols="30" rows="10" 
      v-model="content"></textarea
      >
      <input type="submit" value="작성" class="commentCreateBtn" />
    </form>
  </div>
</template>
  
  <script>
import axios from "axios";
const API_URL = "http://localhost:8000";

export default {
  name: "CommentCreateView",
  data() {
    return {
      content: null,
    };
  },
  props: {
    article_id: Number,
    article : Object
  },
  methods: {
    createComment() {
      if (!this.content) {
        alert("내용을 입력해주세요");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/community/articles/${this.article_id}/comments/`,
        data: {
          content: this.content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
            
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
  
<style>
@import "@/style/article.css";
</style>
  