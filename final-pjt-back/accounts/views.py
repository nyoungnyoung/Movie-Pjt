from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, GuestbookSerializer
from community.serializers import ArticleSerializer,CommentSerializer
from movies.serializers import MovieSerializer, ReviewSerializer
from .models import User, Guestbook
from movies.models import Moviecup
from community.models import Article, Comment
from movies.models import Movie,Review
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.core.files.storage import FileSystemStorage

@api_view(['GET'])
def all_user(request):      # 전체유저정보 조회
    User=get_user_model()
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user(request, username):
    User=get_user_model()
    user = User.objects.get(username = username)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def update_user(request, username):
    User=get_user_model()
    intro = request.data['introduction']
    name = request.data['realname']
    user = User.objects.get(username = username)
    user.introduction = intro
    user.name = name
    user.save()
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def upload_image(request,username):
    user = User.objects.get(username = username)
    print(user)
    # user.image = request.FILES['image']
    # user.save()
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def follow(request, username):
    User = get_user_model()
    me = request.user
    you = User.objects.get(username = username)
    if me != you:
        # 내가(request.user) 그 사람의 팔로워 목록에 있다면
        if me in you.followers.all():
            # 언팔로우
            you.followers.remove(me)
            follow = False
        else:
            # 팔로우
            you.followers.add(me)
            follow = True
        follow_status = {
            'follow': follow,
            'followings': you.followings.count(),
            'followers': you.followers.count()
        }
    return Response(follow_status)

@api_view(['GET'])
def get_profile_info(request,username):
    User = get_user_model()
    me = request.user
    you = User.objects.get(username = username)
    if me in you.followers.all():
        follow = True
    else:
        follow = False
    like_articles = ArticleSerializer(you.like_articles.all(),many=True)
    like_comments = CommentSerializer(you.like_comments.all(),many=True)
    like_movies = MovieSerializer(you.like_movies,many=True)
    like_reviews = ReviewSerializer(you.like_reviews,many=True)
    articles = ArticleSerializer(Article.objects.filter(user=you),many=True)
    reviews = ReviewSerializer(Review.objects.filter(user=you),many=True)
    comments = CommentSerializer(Comment.objects.filter(user=you),many=True)
    follow_status = {
            'follow': follow,
            'followings': you.followings.count(),
            'followers': you.followers.count(),
            'like_articles': like_articles.data,
            'like_comments' : like_comments.data,
            'like_movies': like_movies.data,
            'like_reviews' : like_reviews.data,
            'articles': articles.data,
            'comments': comments.data,
            'reviews': reviews.data,
        }
    return Response(follow_status)

@api_view(['GET'])
def get_moviecup_info(request):
    moviecups= Moviecup.objects.filter(user=request.user)
    if moviecups:
        moviecup = moviecups.order_by('-created_at').moviecup[0]    
        serializer = MovieSerializer(Movie.objects.get(pk=moviecup.movie.id))
        return Response(serializer.data) 
    else : 
        return
    

#방명록
@api_view(['GET','POST'])
def guestbook(request,username):
    User = get_user_model()
    user = User.objects.get(username=username)

    if request.method == 'GET':
        books = Guestbook.objects.filter(to_user=user)
        if books:
            books=books.order_by('-created_at')
        serializer = GuestbookSerializer(books, many= True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = GuestbookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(to_user=user, from_user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
