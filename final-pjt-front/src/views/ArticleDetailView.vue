<template>
  <div class="articleContainer">
    <b-card>
      <h1 class="articleTitle">{{ article?.title }}</h1>
      <hr />
      <div class="d-flex justify-content-between">
        <h5 class="articleUser" @click="toProfile">
          <b-icon icon="person-fill" style="margin-right: 5px"></b-icon
          >{{ article?.username }}
        </h5>
        <h6 class="articleDate">{{ article?.created_at }}</h6>
      </div>
      <hr />
      <div class="articleContent">
        <h5>{{ article?.content }}</h5>
      </div>
      <hr />
      <div class="d-flex justify-content-between">
        <div>
          <p @click.stop="likeArticle">
            <span>{{ like }}</span> <span>{{ like_count }}</span>
          </p>
        </div>
        <div v-show="same_user">
          <button class="articleBtn" @click="deleteArticle">삭제</button>
          <button class="articleBtn" @click="updateArticle">수정</button>
        </div>
      </div>
    </b-card>

    <b-avatar
      v-b-toggle.collapseComment
      id="commentBtn"
      icon="chat-square-dots-fill"
    ></b-avatar>
    <form @submit.prevent="createComment" id="commentForm" class="d-flex justify-content-between">
      <textarea 
      @keydown.enter.prevent="createComment"
      placeholder = '댓글을 입력하세요'
      id="content" cols="30" rows="10" 
      v-model="content"></textarea
      >
    </form>
    <CommentListItem v-for="(comment,idx) in comments" :key="idx" :comment="comment"
    :article="article"/>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";
const API_URL = "http://localhost:8000";
import CommentListItem from '@/components/CommentListItem.vue'
export default {
  name: "ArticleDetailView",
  data() {
    return {
      article_id: this.$route.params.article_id,
      article: null,
      is_like: false,
      like_count: _.size(this.movie?.like_users),
      content:null,
      comments:null,
      same_user:false,
    };
  },
  components: {
    CommentListItem
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
    get_is_like() {
      if (this.article?.like_users.includes(this.user.pk)) {
        this.is_like = true;
      } else {
        this.is_like = false;
      }
    },
    getComments(){
      axios({
        method: 'get',
        url: `${API_URL}/community/articles/${this.article_id}/comments/`,
      }).then((response) => {
        this.comments=response.data
      }).catch((error) => {
        console.log(error)
      })
    },
    getArticle() {
      axios({
        method: "get",
        url: `${API_URL}/community/article/${this.article_id}/`,
      })
        .then((response) => {
          const user = this.$store.getters.getUser
          this.article = response.data;
          if(this.article.user==user.pk){
            this.same_user=true
          }else{
            this.same_user=false
          }
          this.like_count = _.size(this.article?.like_users);
          if (this.$store.state.token) {
            this.get_is_like();
          }
          this.getComments()
        })
        .catch((error) => {
          console.log(error);
        });
    },
    updateArticle() {
      return this.$router.push({
        name: "ArticleUpdateView",
        params: { article: this.article },
      });
    },
    deleteArticle() {
      axios({
        method: "delete",
        url: `${API_URL}/community/article/${this.article_id}/`,
      })
        .then(() => {
          alert("게시글이 삭제되었습니다.");
          this.$router.push({ name: "CommunityView" });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    likeArticle() {
      axios({
        method: "post",
        url: `${API_URL}/community/article/${this.article_id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          this.is_like = response.data["like"];
          this.like_count = response.data["like_count"];
        })
        .catch((error) => {
          console.log(error);
        });
    },
    toProfile() {
      this.$router.push({
        name: "ProfileView",
        params: { username: this.article?.username },
      });
    },
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
          this.getComments()
          this.content=''
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getArticle();
  },
};
</script>

<style>
@import "@/style/article.css";
</style>
