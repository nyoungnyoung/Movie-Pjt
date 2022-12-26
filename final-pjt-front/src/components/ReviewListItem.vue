<template>
  <div>
    <div id="reviewListItem">
      <div class="d-flex justify-content-between" id="reviewHead">
        <router-link
          :to="{ name: 'ProfileView', params: { username: review?.username } }"
          >{{ review?.username }}</router-link
        >
        <p @click="like_review">{{ like }} {{ like_count }}</p>
      </div>
      <div id="reviewContent">
        {{ review?.content }}
      </div>
      <div v-show="same_user">
        <div class="d-flex justify-content" >
        <button v-show="!updateBox" @click="updateReviewBox" class="reviewBtn">수정</button>
        <button @click="deleteReview" class="reviewBtn">삭제</button>
      </div>
      <form v-if="updateBox" @submit.prevent="updateReview" id="reviewUpdate">
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea
        ><br />
        <input type="submit" value="수정" class="reviewBtn" />
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
  name: "ReviewListItem",
  props: {
    review: Object,
  },
  data() {
    return {
      content: this.review?.content,
      updateBox: false,
      is_like: false,
      like_count: _.size(this.review?.like_users),
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
      if(this.review.user==user.pk){
        this.same_user=true
      }else{
        this.same_user=false
      }
    },
    get_is_like() {
      if (this.$store.state.token) {
        if (this.review?.like_users.includes(this.user.pk)) {
          this.is_like = true;
        } else {
          this.is_like = false;
        }
      }
    },
    deleteReview() {
      axios({
        method: "delete",
        url: `${API_URL}/movies/reviews/${this.review?.id}/`,
      })
        .then(() => {
          alert("리뷰가 삭제되었습니다.");
          this.$router.go(this.$router.currentRoute);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    updateReview() {
      if (!this.content) {
        alert("내용을 입력해주세요");
        return;
      }
      axios({
        method: "put",
        url: `${API_URL}/movies/reviews/${this.review?.id}/`,
        data: {
          content: this.content,
        },
      })
        .then(() => {
          alert("리뷰가 수정되었습니다.");
          this.$router.go(this.$router.currentRoute);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    updateReviewBox() {
      this.updateBox = !this.updateBox;
    },
    like_review() {
      if (!this.$store.state.token) {
        alert("로그인하세요");
        return;
      } else {
        axios({
          method: "post",
          url: `${API_URL}/movies/review/${this.review?.id}/like/`,
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
  },
  created() {
    this.check()
    if (this.$store.state.token) {
      this.get_is_like();
    }
  },
};
</script>

<style>
@import "@/style/movie.css";
</style>
