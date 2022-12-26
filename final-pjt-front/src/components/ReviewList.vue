<template>
  <div>
    <form
      @submit.prevent="createReview"
      id="reviewForm"
    >
      <textarea
        placeholder="리뷰을 입력하세요"
        id="reviewContent"
        cols="30"
        rows="10"
        v-model="content"></textarea>
      <input type="submit" value="리뷰 작성" class="reviewCreateBtn" />
    </form>
    <ReviewListItem
      v-for="review in reviews"
      :review="review"
      :key="review?.id"
    />
  </div>
</template>
<script>
import ReviewListItem from "@/components/ReviewListItem";
import axios from 'axios'
const API_URL = "http://localhost:8000"

export default {
  name: "ReviewList",
  components: {
    ReviewListItem,
  },
  data(){
    return{
      reviews:null,
      content: null,
    }
  },
  props:{
    movie_id : Number,
    movie : Object
  },
  methods: {
    getReviews(){
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.movie_id}/review/`,
      }).then((response) => {
        this.reviews=response.data
  
      }).catch((error) => {
        console.log(error)
      })
    },
    createReview() {
      if (!this.content) {
        alert("내용을 입력해주세요");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/movies/${this.movie_id}/review/`,
        data: {
          content: this.content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.getReviews()
          this.content=''
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getReviews();
  },
};
</script>

<style>
@import '@/style/movie.css';
</style>