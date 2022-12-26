<template>
  <div>
    <div id="commentListItem">
      <div class="d-flex justify-content-between" id="commentHead">
        <router-link
          :to="{ name: 'ProfileView', params: { username: comment?.username } }"
          >{{ comment?.username }}</router-link
        >
        <p @click="likeComment">{{ like }} {{ like_count }}</p>
      </div>
      <div id="commentContent">
        {{ comment?.content }}
      </div>
      <div v-show="same_user">
        <div class="d-flex justify-content">
          <button @click="updateCommentBox" class="commentBtn">수정</button>
          <button @click="deleteComment" class="commentBtn">삭제</button>
        </div>
        <form v-if="updateBox" @submit.prevent="updateComment" id="commentUpdate">
          <textarea id="content" cols="30" rows="10" v-model="content"></textarea
            ><br />
            <input type="submit" value="수정" class="commentBtn" />
          </form>
        </div>
      </div>

    <form class="d-flex justify-content-between">
      <input @keydown.enter.prevent="createRecomment" type="text" v-model="re_content" id="content" placeholder = '대댓글을 입력하세요'/>
      <button @click.prevent="createRecomment" class="recommentCreateBtn" >작성</button>
    </form>
    <RecommentList
      :recomments="recomments"
      :comment="comment"
      :article="article"
    />
    <hr />
  </div>
</template>

<script>
import _ from "lodash";
import axios from "axios";
import RecommentList from "@/components/RecommentList.vue";
const API_URL = "http://localhost:8000";

export default {
  name: "CommentListItem",
  components: {
    RecommentList,
  },
  props: {
    comment: Object,
    article: Object,
  },
  data() {
    return {
      content: this.comment.content,
      updateBox: false,
      is_like: false,
      like_count: _.size(this.comment.like_users),
      recomments: null,
      re_content: null,
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
      if(this.comment.user==user.pk){
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
    deleteComment() {
      axios({
        method: "delete",
        url: `${API_URL}/community/comments/${this.comment?.id}/`,
      })
        .then(() => {
          alert("댓글이 삭제되었습니다.");
          this.$router.go(this.$router.currentRoute);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    updateComment() {
      if (!this.content) {
        alert("내용을 입력해주세요");
        return;
      }
      axios({
        method: "put",
        url: `${API_URL}/community/comments/${this.comment?.id}/`,
        data: {
          content: this.content,
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
    updateCommentBox() {
      this.updateBox = !this.updateBox;
    },
    likeComment() {
      axios({
        method: "post",
        url: `${API_URL}/community/comment/${this.comment?.id}/like/`,
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
    },
    getRecomments() {
      axios({
        method: "get",
        url: `${API_URL}/community/comment/${this.article?.id}/${this.comment?.id}/`,
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
        url: `${API_URL}/community/comment/${this.article?.id}/${this.comment?.id}/`,
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
  },
  watch:{
    comment(){
      this.getRecomments()
    }
  },
  created() {
    this.get_is_like();
    this.getRecomments();
    this.check();
  },
};
</script>

<style>
@import "@/style/article.css";
</style>
