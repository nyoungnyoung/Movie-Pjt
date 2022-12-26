<template>
  <div>
    <CommentListItem
      v-for="comment in comments"
      :comment = "comment"
      :article = "article"
      :key="comment.id"
    />
  </div>
</template>
<script>
import CommentListItem from "@/components/CommentListItem";
import axios from 'axios'
const API_URL = "http://localhost:8000"

export default {
  name: "CommentList",
  components: {
    CommentListItem,
  },
  data(){
    return{
      comments:null,
    }
  },
  props:{
    article_id : Number,
    article : Object
  },
  methods: {
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
  },
  created() {
    this.getComments();
  },
};
</script>

<style>
</style>