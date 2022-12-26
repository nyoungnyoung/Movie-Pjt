from django.urls import path
from . import views

app_name = 'accounts' #accountsinfo

urlpatterns = [
    path('', views.all_user),
    path('<str:username>/', views.get_user),
    path('<str:username>/update/', views.update_user),
    path('<str:username>/info/', views.get_profile_info),
    path('<str:username>/guestbook/', views.guestbook),
    path('moviecup/', views.get_moviecup_info),
    path('follow/<str:username>/', views.follow),
    path('<str:username>/hihi/',views.upload_image),
]