<template>
  <div>
    <b-container fluid style="width: 90%">
      <b-row>
        <b-col offset-md="2">
          <hr class="my-4" />
          <h1>Profile</h1>
        </b-col>
      </b-row>
      <b-row align-h="center">
        <b-col cols="6" md="2" class="my-4">
          <img id="profileimage" src="../../../사진/iu.png" alt="" />
          <div class="name">
            <b-avatar icon="person" />{{ profileUser?.username }}
          </div>
        </b-col>

        <b-col cols="12" md="10">
          <b-tabs content-class="mt-3" card id="app">
            <b-tab title="프로필 정보" active>
              <b-list-group>
                <b-list-group-item>
                  <span class="p-1 mr-3">
                    <b-avatar icon="person" /> {{ profileUser?.name
                    }}<span class="text-secondary">
                      (가입날짜 : {{ profileUser?.date_joined.substr(0, 10) }},
                      최근접속일 : {{ profileUser?.last_login.substr(0, 10) }})
                    </span>
                  </span>
                </b-list-group-item>

                <b-list-group-item>
                  <span class="p-1 mr-3">
                    <b-avatar icon="people" />
                    <span class="m-2"> following : {{ followings }} </span>|
                    <span class="m-2"> followers : {{ followers }} </span>
                  </span>
                </b-list-group-item>
                <b-list-group-item>
                  <span class="p-1">
                    <b-avatar icon="list-ul" />
                    <span class="m-2"> review : {{ reviews?.length }}</span
                    >| <span class="m-2"> article : {{ articles?.length }}</span
                    >|
                    <span class="m-2">
                      comment : {{ comments?.length }}</span
                    ></span
                  >
                </b-list-group-item>
                <b-list-group-item>
                  <span class="p-1">
                    <b-avatar icon="bookmark-heart" />
                    <span class="m-2"> movie : {{ like_movies?.length }}</span
                    >|
                    <span class="m-2"> review : {{ like_reviews?.length }}</span
                    >|
                    <span class="m-2">
                      article : {{ like_articles?.length }}</span
                    >|
                    <span class="m-2">
                      comment : {{ like_comments?.length }}</span
                    ></span
                  >
                </b-list-group-item>
                <b-list-group-item>
                  <span class="p-1 mr-3">
                    <b-avatar icon="chat-right-dots" />{{
                      profileUser?.introduction
                    }}
                  </span>
                </b-list-group-item>
              </b-list-group>
              <br />
              <button
                @click="editProfile"
                v-show="!is_other"
                class="btn btn-outline-dark"
                sytle="width:200px;"
              >
                <b-avatar icon="person-circle" />
                프로필 편집
              </button>
            </b-tab>
            <b-tab title="방명록" @click="getGuestbook">
              <b-list-group-item style="padding-top: 25px">
                <b-avatar icon="chat-quote" />
                <h5>방명록 작성하기</h5>
                <b-form-input
                  :placeholder="`${profileUser?.username}님께 방명록을 남겨보세요!`"
                  style="
                    width: 70%;
                    height: 60px;
                    margin: 10px;
                    margin-left: 15%;
                  "
                  @keydown.enter.prevent="setGuestbook"
                  type="text"
                  v-model="guestbook_content"
                />
              </b-list-group-item>
              <b-list-group
                style="padding: 2%; height: 400px; margin: 20px; overflow: scroll"
              >
                <TalkLeftItem
                  v-for="(book, idx) in from_profile_books"
                  :key="idx"
                  :item="book"
                />
                <TalkRightItem
                  v-for="(book, idx) in to_profile_books"
                  :key="idx"
                  :item="book"
                />
              </b-list-group>
            </b-tab>
            <b-tab title="리뷰" @click="getGuestbook">
              <b-list-group-item style="padding-top: 25px">
                <b-avatar icon="chat-quote" />
                <h5>{{ profileUser?.username }}님이 작성한 리뷰</h5>
              </b-list-group-item>
              <b-list-group-item
                style="padding: 2%; height: 500px; overflow: scroll"
              >
              <TalkItem
            style="width: 100%"
            v-for="(review, idx) in reviews"
            :key="idx"
            :item="review"
          />
              </b-list-group-item>
            </b-tab>
          </b-tabs>
          <button
            v-show="is_other"
            type="button"
            class="btn btn-outline-dark"
            @click="followUser"
          >
            <b-avatar v-if="!is_follow" icon="person-plus" />
            <b-avatar v-if="is_follow" icon="person-dash" />
            {{ fol_or_unfol }}
          </button>
          <div class="flexcontainer"></div>
        </b-col>
      </b-row>
    </b-container>
    <div style="width: 70%; margin-left: 20%; margin-top: 3%">
      <h3 style="margin-left: 10%">
        💗 {{ profileUser?.username }}님이 좋아하는 영화 💗
      </h3>
      <p @click="goLikeMovies" style="text-align: end; font-size: small">
        <b-avatar icon="reply-all" />전체보기
      </p>
      <!--좋아하는 영화-->
      <div class="like_movies_container">
        <MovieList :movies="like_movies" />
      </div>
    </div>
    <div
      class="flexcontainer"
      style="padding: 50px; width: 75%; margin-left: 12%"
    >
      <!--좋아하는 리뷰-->
      <b-container
        style="width: 45%; flex-direction: column; justify-content: flex-start"
      >
        <h3 style="margin-right: 30px; width: 100%">
          💗 {{ profileUser?.username }}님이 좋아하는 리뷰 💗
        </h3>
        <div
          style="
            height: 600px;
            overflow: scroll;
            overflow-x: hidden;
            padding: 20px;
            margin-right: 20px;
          "
        >
          <TalkItem
            style="width: 100%"
            v-for="(review, idx) in like_reviews"
            :key="idx"
            :item="review"
          />
        </div>
      </b-container>
      <!--좋아하는 게시글-->
      <b-container
        style="width: 45%; flex-direction: column; justify-content: flex-start"
      >
        <h3 style="margin-right: 30px; width: 100%">
          💗 {{ profileUser?.username }}님이 좋아하는 게시글 💗
        </h3>
        <div
          style="
            height: 600px;
            overflow: scroll;
            overflow-x: hidden;
            padding: 20px;
            margin-right: 20px;
          "
        >
          <TalkItem
            style="width: 100%"
            v-for="(article, idx) in like_articles"
            :key="idx"
            :item="article"
          />
        </div>
      </b-container>
    </div>
    <div
      class="flexcontainer"
      style="padding: 50px; width: 75%; margin-left: 12%"
    >
      <b-container
        style="width: 45%; flex-direction: column; justify-content: flex-start"
      >
        <h3 style="margin-right: 30px; width: 100%">
          <b-avatar icon="list-ul" />{{ profileUser?.username }}님이 작성한
          게시글
        </h3>
        <div
          style="
            height: 600px;
            overflow: scroll;
            overflow-x: hidden;
            padding: 20px;
            margin-right: 20px;
          "
        >
          <TalkItem
            style="width: 100%"
            v-for="(article, idx) in articles"
            :key="idx"
            :item="article"
          />
        </div>
      </b-container>
      <b-container
        style="width: 45%; flex-direction: column; justify-content: flex-start"
      >
        <h3 style="margin-right: 30px; width: 100%">
          <b-avatar icon="list-ul" />{{ profileUser?.username }}님이 작성한 댓글
        </h3>
        <div
          style="
            height: 600px;
            overflow: scroll;
            overflow-x: hidden;
            padding: 20px;
            margin-right: 20px;
          "
        >
          <TalkItem
            style="width: 100%"
            v-for="(article, idx) in comments"
            :key="idx"
            :item="article"
          />
        </div>
      </b-container>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://localhost:8000";
import MovieList from "@/components/MovieList.vue";
import TalkLeftItem from "@/components/TalkLeftItem.vue";
import TalkRightItem from "@/components/TalkRightItem.vue";
import TalkItem from "@/components/TalkItem.vue";
export default {
  name: "ProfileView",
  components: {
    MovieList,
    TalkLeftItem,
    TalkRightItem,
    TalkItem,
  },
  data() {
    return {
      profileUser: null,
      is_follow: null,
      followers: null,
      followings: null,
      like_articles: null,
      like_comments: null,
      like_movies: null,
      like_reviews: null,
      articles: null,
      comments: null,
      reviews: null,
      moviecup: null,
      introduction: "자기소개가 없습니다.",
      realname: "이름이 없습니다.",
      profile_image_url: null,
      ////
      guestbooks: null,
      guestbook_content: null,
      from_profile_books: [],
      to_profile_books: [],
    };
  },
  computed: {
    username() {
      return this.$route.params.username;
    },
    loginUser() {
      return this.$store.getters.getUser;
    },
    is_other() {
      if (this.loginUser?.username != this.profileUser?.username) {
        return true;
      } else {
        return false;
      }
    },
    fol_or_unfol() {
      return this.is_follow ? "언팔로우" : "팔로우";
    },
  },
  methods: {
    followUser() {
      if (this.loginUser.username != this.profileUser.username) {
        axios({
          method: "post",
          url: `${API_URL}/accountsinfo/follow/${this.username}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((response) => {
            this.is_follow = response.data["follow"];
            this.followers = response.data["followers"];
            this.followings = response.data["followings"];
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    setUser() {
      axios({
        method: "post",
        url: `${API_URL}/accountsinfo/${this.username}/update/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: {
          introduction: this.introduction,
          realname: this.realname,
        },
      })
        .then(() => {
          this.getUserInfo();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    editProfile() {
      this.$router.push({
        name: "ProfileEditView",
        params: { username: this.username },
      });
    },
    getUserInfo() {
      axios({
        method: "get",
        url: `${API_URL}/accountsinfo/${this.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          this.profileUser = response.data;
          this.introduction = this.profileUser?.introduction;
          this.realname = this.profileUser?.name;
          this.profile_image_url = this.profileUser?.profile_image_url;
          this.getFollowInfo();
        })
        .catch(() => {
          alert("존재하지 않는 사용자입니다.");
          this.$router.go(-1);
        });
    },
    getFollowInfo() {
      axios({
        method: "get",
        url: `${API_URL}/accountsinfo/${this.username}/info/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          this.is_follow = response.data["follow"];
          this.followers = response.data["followers"];
          this.followings = response.data["followings"];
          this.like_articles = response.data["like_articles"];
          this.like_comments = response.data["like_comments"];
          this.like_movies = response.data["like_movies"];
          this.like_reviews = response.data["like_reviews"];
          this.articles = response.data["articles"];
          this.comments = response.data["comments"];
          this.reviews = response.data["reviews"];
          this.moviecup = response.data["moviecup"];
        })
        .catch((error) => {
          console.log(error);
        });
    },
    genreRecommend() {
      if (this.like_movies.length == 0) {
        alert("영화 좋아요 해야 추천 가능!!");
      } else {
        this.$router.push({ name: "RecommendGenreView" });
      }
    },
    goLikeMovies() {
      this.$router.push({
        name: "LikeMovieView",
        params: { username: this.username },
      });
    },
    getGuestbook() {
      axios({
        method: "get",
        url: `${API_URL}/accountsinfo/${this.username}/guestbook/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          this.guestbooks = response.data;
          let temp_from = [];
          let temp_to = [];
          this.guestbooks.forEach((book) => {
            if (book.from_user == this.profileUser.id) {
              temp_from.push(book);
            } else if (book.to_user == this.profileUser.id) {
              temp_to.push(book);
            }
          });
          this.to_profile_books = temp_to;
          this.from_profile_books = temp_from;
        })
        .catch(() => {});
    },
    setGuestbook() {
      axios({
        method: "post",
        url: `${API_URL}/accountsinfo/${this.username}/guestbook/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: {
          content: this.guestbook_content,
        },
      })
        .then(() => {
          this.guestbook_content = "";
          this.getGuestbook();
        })
        .catch(() => {});
    },
  },
  created() {
    this.getUserInfo();
  },
};
</script>

<style>
body {
  -ms-overflow-style: none;
}

::-webkit-scrollbar {
  display: none;
}
#profileimage {
  width: 80%;
  border-radius: 50%;
  border: 5px solid rgb(255, 254, 252);
}
.name {
  font-size: xx-large;
}
.like_movies_container {
  background-color: white;
  height: 1090px;
  overflow: hidden;
  border: 1px solid rgb(201, 201, 201);
  border-radius: 10px;
}
.flexcontainer {
  display: flex;
  justify-content: flex-end;
}

</style>