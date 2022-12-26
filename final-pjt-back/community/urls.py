from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('',views.article_list),
    path('article/<int:article_id>/', views.article),
    path('<int:board_number>/', views.board_list),
    path('create/', views.article_create),
    path('comments/<int:comment_id>/', views.comment_detail),
    path('comment/<int:comment_id>/like/',views.like_comment),
    path('comment/<int:article_id>/<int:parent_id>/',views.recomment),
    path('comments/<int:parent_id>/<int:comment_id>/', views.recomment_detail),
    path('articles/<int:article_id>/comments/', views.comment),
    path('article/<int:article_id>/like/',views.like_article),
]

