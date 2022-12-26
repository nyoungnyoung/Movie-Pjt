<template>
  <div>
    <b-table hover
      class="table"
      id="articlestable"
      :fields="fields"
      :items="articles"
      :per-page="perPage"
      :current-page="currentPage"
      @row-clicked="toDetail"
    >
      <!-- <thead>
        <tr>
          <th scope="col" style="width: 3rem">No</th>
          <th scope="col" style="width: 30rem">제목</th>
          <th scope="col" style="width: 8rem">작성자</th>
          <th scope="col" style="width: 8rem">날짜</th>
        </tr>
      </thead> -->
      <tbody>
        <!-- <ArticleListItem
          v-for="article in articles"
          :article="article"
          :key="article.id"
        /> -->
      </tbody>
    </b-table>
    <div class="pageToggle d-flex justify-content-center">
    <b-pagination
      v-model="currentPage"
      :total-rows="allArticles"
      :per-page="perPage"
      aria-controls="articlestable"
      btn-warning
    ></b-pagination>
    </div>
  </div>
</template>
<script>
// import ArticleListItem from "@/components/ArticleListItem";

export default {
  name: "ArticleList",
  components: {
    // ArticleListItem,
  },
  data() {
    return {
      ArticleData: [],
      currentPage: 1,
      perPage: 10,
      articleNo: 0,
      fields: [
        { key: "id", 
          label: "No" , 
          thClass: "numField",
          // formatter: () => {
          // this.articleNo += 1
          // return this.articleNo
          // }
        },
        { key: this.articleNo, label: "test"},
        { key: "title", 
          label: "제목" , 
          thClass: "titleField",
          formatter: (value) => {
            if (value.length >= 30) {
              return value.substr(0, 30) + '...'
            } else {
              return value
            }
          }},
        { key: "username", label: "작성자" , thClass: "nameField"},
        {
          key: "created_at",
          label: "날짜",
          thClass: "dateField",
          formatter: (value) => {
            return value.substr(0, 10);
          },
        },
        {
          key: "like_users",
          label: "추천",
          thClass:"likeField",
          formatter: (value) => {
            return value.length;
          },
        },
      ],
    };
  },
  computed: {
    articles() {
      return this.$store.getters.getArticles;
    },
    allArticles() {
      return this.$store.getters.getArticles.length;
    },
    // sortedData() {
    //   return this.$store.getters.getArticles.articles.sort((a,b) => {return b.id - a.id})
    // }
  },
  props: {
    board_number: Number,
  },
  // mounted() {
  //   this.pageMethod(this.currentPage);
  // },
  methods: {
    getArticles() {
      this.$store.dispatch("getArticles", this.board_number);
    },
    // getPageData() {
    //   const tmp = {};
    //   this.ArticleData = tmp;
    // },
    toDetail(item) {
      if(!this.$store.state.token){
        alert('로그인하세요')
        this.$router.push({ name: "LogInView" }) 
      }
      else{
      this.$router.push({
        name: "ArticleDetailView",
        params: { article_id: item.id },
      });}
    },
    // pageMethod(currentPage) {
    //   this.currentData = this.articles.slice(
    //     (currentPage - 1) * this.limitArticles,
    //     currentPage * this.limit
    //   );
    //   this.currentPage = currentPage;
    //   console.log(this.currentData, this.currentPage);
    // },
  },
  created() {
    this.getArticles();
  },
  watch: {
    board_number() {
      this.getArticles();
    },
  },
};
</script>

<style>
#articlestable {
  width: 80vw;
  vertical-align: middle;
}
.numField {
  width: 50px
}
.titleField{
  width: 40vw
}
.nameField{
  width: 130px
}
.dateField{
  width: 120px
}
.likeField{
  width: 60px
}
</style>