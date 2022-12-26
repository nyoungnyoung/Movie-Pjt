<template>
  <div id="recomment">
    <div id="recommentListItem">
      <div
        class="d-flex justify-content-between flex-row-reverse"
        id="recommentHead"
      >
        <router-link
          :to="{
            name: 'ProfileView',
            params: { username: recomment?.username },
          }"
          >{{ recomment?.username }}</router-link
        >
        <p @click="likeComment">{{ like }} {{ like_count }}</p>
      </div>
      <div id="recommentContent">
        {{ recomment?.content }}
      </div>

<div v-show="same_user">

  <div class="d-flex justify-content-end">
    <button @click="updateReCommentBox" class="recommentBtn">수정</button>
    <button @click="deleteReComment" class="recommentBtn">삭제</button>
  </div>
  <form
  v-if="updateBox"
  @submit.prevent="updateReComment"
  id="commentUpdate"
  >
  <textarea
  id="content"
  cols="30"
  rows="10"
  v-model="re_content"
  ></textarea
  ><br />
  <input type="submit" value="수정" class="recommentBtn" />
</form>
</div>
</div>

  </div>
</template>

<script>
import _ from "lodash";
import axios from "axios";
const API_URL = "http://localhost:8000";

export default {
  name: "RecommentListItem",
  props: {
    recomment: Object,
    article: Object,
    comment: Object,
  },
  data() {
    return {
      recomments: null,
      re_content: this.recomment.content,
      updateBox: false,
      is_like: null,
      like_count: _.size(this.comment.like_users),
      same_user:false,
    };
  },
  computed: {
    user() {
      return this.$store.getters.getUser;
    },
    like() {
      return this.is_like ? "❤️" : "🤍";
    },
  },
  methods: {
    check(){
      const user = this.$store.getters.getUser
      if(this.recomment.user==user.pk){
        this.same_user=true
      }else{
        this.same_user=false
      }
    },
    get_is_like() {
      if (this.comment.like_users.includes(this.user.pk)) {
        this.is_like = true;
      } else {
        this.is_like = false;
      }
    },
    likeComment() {
      if (!this.$store.state.token) {
        alert("로그인하세요");
        return;
      } else {
        axios({
          method: "post",
          url: `${API_URL}/community/comment/${this.recomment.id}/like/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            this.is_like = res.data["like"];
            this.like_count = res.data["like_count"];
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    getRecomments() {
      axios({
        method: "get",
        url: `${API_URL}/community/comment/${this.article?.id}/${this.recomment?.id}/`,
      })
        .then((response) => {
          this.recomments = response.data;
  
        })
        .catch((error) => {
          console.log(error);
        });
    },
    createRecomment() {
      axios({
        method: "post",
        url: `${API_URL}/community/comment/${this.article?.id}/${this.recomment?.id}/`,
        data: {
          content: this.re_content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.re_content = "";
          this.getRecomments();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deleteReComment() {
      axios({
        method: "delete",
        url: `${API_URL}/community/comments/${this.recomment.id}/`,
      })
        .then(() => {
          alert("댓글이 삭제되었습니다.");
          this.$router.go(this.$router.currentRoute);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    updateReCommentBox() {
      this.updateBox = !this.updateBox;
    },
    updateReComment() {
      if (!this.re_content) {
        alert("내용을 입력해주세요");
        return;
      }
      axios({
        method: "put",
        url: `${API_URL}/community/comments/${this.comment.id}/${this.recomment.id}/`,
        data: {
          content: this.re_content,
        },
      })
        .then(() => {
          alert("댓글이 수정되었습니다.");
          this.$router.go(this.$router.currentRoute);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.check();
    this.getRecomments();
  },
};
</script>

<style></style>
