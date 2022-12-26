import Vue from "vue";
import VueRouter from "vue-router";
import MainMovieView from "@/views/MainMovieView.vue";
import MovieView from "@/views/MovieView.vue";
import MovieDetailView from '@/views/MovieDetailView.vue'
import CommunityView from '@/views/CommunityView'
import ArticleDetailView from '@/views/ArticleDetailView'
import ArticleCreateView from '@/views/ArticleCreateView'
import ArticleUpdateView from '@/views/ArticleUpdateView'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ProfileView from '@/views/ProfileView.vue'
import TopMovieDetailView from '@/views/TopMovieDetailView'
import SearchMovieView from '@/views/SearchMovieView'
import RecommendGenreView from '@/views/RecommendGenreView'
import MoviecupView from '@/views/MoviecupView'
import ProfileEditView from '@/views/ProfileEditView'
import LikeMovieView from '@/views/LikeMovieView'
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "MainMovieView",
    component: MainMovieView,
  },
  {
    path: "/movie/",
    name: "MovieView",
    component: MovieView,
  },
  {
    path: "/movie/:movie_id/",
    name: "MovieDetailView",
    component: MovieDetailView,
  },
  {
    path: '/community/',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: "/community/article/:article_id/",
    name: "ArticleDetailView",
    component: ArticleDetailView,
  },
  {
    path: "/community/article/create/",
    name: "ArticleCreateView",
    component: ArticleCreateView
  },
  {
    path: "/community/article/update/",
    name: "ArticleUpdateView",
    component: ArticleUpdateView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  {
    path: '/profile/:username/',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path : '/topmovies/:movie_id',
    name : 'TopMovieDetailView',
    component : TopMovieDetailView
  },
  {
    path : '/searchMovie',
    name : 'SearchMovieView',
    component : SearchMovieView
  },
  {
    path : '/recommendGenre',
    name : 'RecommendGenreView',
    component : RecommendGenreView
  },
  {
    path : '/moviecup',
    name : 'MoviecupView',
    component : MoviecupView
  },
  {
    path : '/profileEdit',
    name : 'ProfileEditView',
    component : ProfileEditView
  },
  {
    path : '/likemovies',
    name : 'LikeMovieView',
    component : LikeMovieView
  }


];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() { 
    return { x: 0, y: 0 } 
  },
});

const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => {
		if (err.name !== 'NavigationDuplicated') throw err;
	});
};
export default router;
