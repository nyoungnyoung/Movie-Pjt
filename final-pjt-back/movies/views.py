from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes      # 나중에 로그인된 사용자만 조회가능한 부분 만들 때
from rest_framework.permissions import IsAuthenticated                  # permission_classes([IsAuthenticated])
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, GenreSerializer, ReviewSerializer
from .models import Movie, Review, Moviecup
import random
import requests

def genre_name_movie(movies):
    for movie in movies :
            temp = []
            for genre in movie['genres']:
                temp.append(genre['name'])
            movie['genres']=temp
    return movies

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    movies = genre_name_movie(serializer.data)
    return Response(movies)


@api_view(['GET'])
def random_movies(request):
    random_movies = Movie.objects.all().order_by('?')[:30]
    new=[]
    for movie in random_movies:
        for genre in movie.genres.all():
            if genre.name !='로맨스' and genre.id!=10749 and movie not in new:
                new.append(movie)      
    serializer = MovieSerializer(new, many=True)
    random_movies = genre_name_movie(serializer.data)
    return Response(random_movies)


@api_view(['GET'])
def get_movie(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    API_KEY = "487b617acdcef17f4628cd13e62a835c"
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie.tmdb_id}/videos?api_key={API_KEY}")
    video = response.json()['results'][0]
    url = 'https://www.youtube.com/embed/' + video['key'] 
    movie.video_url = url
    movie.save()
    serializer = MovieSerializer(movie)
    movie = serializer.data
    temp=[]
    for genre in movie['genres']:
        temp.append(genre['name'])
    movie['genres']=temp
    return Response(movie)


@api_view(['GET','POST'])
def review(request,movie_id): #리뷰조회, 작성
    movie = Movie.objects.get(pk = movie_id)
    reviews = Review.objects.filter(movie = movie)
    if reviews : 
        reviews = reviews.order_by('-created_at')
    
    if request.method == 'GET':
        serializer = ReviewSerializer(reviews, many= True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_id):
    review = Review.objects.get(pk=review_id)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def like_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
        like = False
    else:
        movie.like_users.add(request.user)
        like = True
    context = {
        'like': like,
        'like_count' : movie.like_users.count()
    }
    return Response(context)

@api_view(['POST'])
def like_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
        like = False
    else:
        review.like_users.add(request.user)
        like = True
    context = {
        'like': like,
        'like_count' : review.like_users.count()
    }
    return Response(context)

@api_view(['POST'])
def like_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
        like = False
    else:
        movie.like_users.add(request.user)
        like = True
    context = {
        'like': like,
        'like_count' : movie.like_users.count()
    }
    return Response(context)


#검색
@api_view(['GET'])
def search_movie_title(request):
    movies = Movie.objects.all()
    search = request.GET.get('search')
    search_movies = movies.filter(title__icontains=search)
    serializer = MovieSerializer(search_movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_movie_overview(request):
    movies = Movie.objects.all()
    search = request.GET.get('search')
    search_movies = movies.filter(overview__icontains=search)
    serializer = MovieSerializer(search_movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_movie_genre(request,genre_id):
    movies = get_list_or_404(Movie)
    movie_lst=[]
    for movie in movies :
        for genre in movie.genres.all():
            if genre.id == genre_id:
                movie_lst.append(movie)
    movie_sort = []
    for like_movie in movie_lst:
        serializer = MovieSerializer(like_movie)
        movie = serializer.data
        movie_sort.append((
            like_movie.like_users.count(),
            like_movie.popularity,
            movie))
    movie_sort.sort(key=lambda x : (-x[0], -x[1]))
    movie_sort = movie_sort[:30]
    recommend_movies=[]
    for movie in movie_sort :
        recommend_movies.append(movie[2])
    context={
        'movies' : recommend_movies
    }
    return Response(context)




#추천
def genre_movie(me,search_genre,movies):
    # 그 장르에 해당하는 영화 다 가져오고
    movie_lst = []
    for movie in movies:
        for genre in movie.genres.all():
            if genre.name == search_genre:
                if movie in me.like_movies.all():
                    continue
                else:
                    movie_lst.append(movie)
    movie_sort = []
    for like_movie in movie_lst:
        serializer = MovieSerializer(like_movie)
        movie = serializer.data
        movie_sort.append((
            like_movie.like_users.count(),
            like_movie.vote_average,
            movie))
    # 그 영화들 중에서 좋아요(1), 평점(2) => 최상단 10개를 뽑아오기
    movie_sort.sort(key=lambda x : (-x[0], -x[1]))
    movie_sort = movie_sort[:8]
    recommend_movies=[]
    for movie in movie_sort :
        recommend_movies.append(movie[2])
    return recommend_movies



@api_view(['GET'])
def genre_recommend(request):
    # 사용자가 좋아요를 누른 영화와 같은 장르의 영화 10개를 추천
    # 평점(2)과 좋아요(1) 기준으로 10개 추천
    movies = get_list_or_404(Movie)
    if request.user.is_authenticated:
        me = request.user
        like_movies = me.like_movies.all()
        like_genre = dict()
        for like_movie in like_movies:
            for genre in like_movie.genres.all():
                if genre.name not in like_genre:
                    like_genre[genre.name] = 1
                else:
                    like_genre[genre.name] += 1
    # 사용자가 누른 좋아요 영화의 장르 카운팅해서 가장 많이 본 장르 정하고
        like_genre = sorted(like_genre.items(),key=lambda x : (-x[1]))
        max_genre_like = like_genre[0][0]
        second_genre_like = like_genre[1][0]
    # 그 장르에 해당하는 영화 다 가져오고
        first_recommend = genre_movie(me,max_genre_like,movies)
        second_recommend = genre_movie(me,second_genre_like,movies)
        
        context = {
            'max_genre_like' : max_genre_like,
            'second_genre_like' : second_genre_like,
            'first_recommend' : first_recommend,
            'second_recommend' : second_recommend
        }
        return Response(context)


@api_view(['GET'])
def candidate(request):
    num = int(request.GET.get('num'))
    random_movies = Movie.objects.all().order_by('?')[:num]
    serializer = MovieSerializer(random_movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def moviecup(request) :
    if request.method =='GET' : 
        movies = Moviecup.objects.filter(user=request.user).order_by('-created_at')
        moviecup=movies[0]
        movie = Movie.objects.get(pk=moviecup.movie.id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method =='POST' : 
        movie_id = request.data["movie_id"]
        movie = Movie.objects.get(pk=movie_id)
        moviecup = Moviecup(movie=movie, user=request.user)
        moviecup.save()
        movie = Movie.objects.get(pk=moviecup.movie.id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

