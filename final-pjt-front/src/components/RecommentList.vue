<template>
  <div>
    <!-- <h3>{{comment?.content}} μ λλκΈ...</h3> -->
    <RecommentListItem
      v-for="recomment in recomments"
      :recomment="recomment"
      :comment="comment"
      :article="article"
      :key="recomment.id"
    />
  </div>
</template>

<script>
import RecommentListItem from '@/components/RecommentListItem.vue'
export default {
    name : 'RecommentList',
    components:{
        RecommentListItem
    },
    props:{
        recomments : Array,
        article : Object,
        comment : Object,
    }

}
</script>

<style>

</style>