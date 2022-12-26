from django.urls import path
from . import views


urlpatterns = [
    #영화
    path('', views.movie_list),
    path('<int:movie_id>/', views.get_movie),
    path('<int:movie_id>/like/', views.like_movie),
    path('<int:movie_id>/review/', views.review),
    #리뷰
    path('reviews/<int:review_id>/', views.review_detail),
    path('review/<int:review_id>/like/',views.like_review),
    #검색
    path('search/title/',views.search_movie_title),
    path('search/overview/',views.search_movie_overview),
    #추천
    path('random/',views.random_movies),
    path('recommend/genre/',views.genre_recommend),
    path('recommend/genre/<int:genre_id>/',views.search_movie_genre),
    #무비컵
    path('candidate/',views.candidate),
    path('moviecup/',views.moviecup),
]

