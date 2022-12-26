<template>
  <div class="container community">
    <div>
    <h1>Community Page</h1>
    <hr>
    <b-button-group>
      <b-button @click="boardChange(0)">전체게시글</b-button>
      <b-button @click="boardChange(1)">자유게시판</b-button>
      <b-button @click="boardChange(2)">영화추천</b-button>
      <b-button @click="boardChange(3)">극장정보</b-button>
    </b-button-group>
    <!-- <ul class="d-flex">
      <li @click="boardChange(0)">전체게시글</li>
      <li @click="boardChange(1)">자유게시판</li>
      <li @click="boardChange(2)">영화추천</li>
      <li @click="boardChange(3)">극장정보</li>
    </ul> -->
    <hr>
    </div>
    <div>
      <ArticleList
      :board_number = boardNumber
      />
    </div>
    <router-link 
    v-if="isLogin" :to="{ name: 'ArticleCreateView' }" class="btn btn-primary">게시글 작성</router-link>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'
export default {
  name: "CommunityView",
  components : {
    ArticleList
  },
  data(){
    return{
      boardNumber : 0,
    }
  },
  computed : {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    boardChange(board_number){
      this.boardNumber = board_number
    }
  },
};
</script>

<style>
@import '@/style/movie.css';
</style>
