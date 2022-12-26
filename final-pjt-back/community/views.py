from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment
from django.contrib.auth import get_user_model


@api_view(['GET'])
def article_list(request): #전체게시판 조회
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def board_list(request,board_number): #각 게시판 조회 (0: 전체, 1:자유, 2:영화추천, 3:극장정보)
    if board_number==0:
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(board_number=board_number)
    if articles :
        articles = articles.order_by('-created_at')
    serializer = ArticleSerializer(articles, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def article_create(request): #글작성
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user = request.user)  
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def article(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET','POST'])
def comment(request,article_id): #댓글 조회, 작성
    article = Article.objects.get(pk = article_id)
    
    if request.method == 'GET':
        comments = Comment.objects.filter(article = article).filter(parent_id=None)
        if comments :
            comments = comments.order_by('-created_at')
        serializer = CommentSerializer(comments, many= True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def like_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
        like = False
    else:
        article.like_users.add(request.user)
        like = True
    context = {
        'like': like,
        'like_count' : article.like_users.count()
    }
    return Response(context)

@api_view(['POST'])
def like_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
        like = False
    else:
        comment.like_users.add(request.user)
        like = True
    context = {
        'like': like,
        'like_count' : comment.like_users.count()
    }
    return Response(context)


@api_view(['GET','POST'])
def recomment(request,article_id,parent_id): 
    article = Article.objects.get(pk=article_id)
    parent_comment = Comment.objects.get(pk=parent_id)
    if request.method == 'GET':
        comments = Comment.objects.filter(parent=parent_comment)
        if comments :
            comments = comments.order_by('-created_at')
        serializer = CommentSerializer(comments, many= True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user, parent = parent_comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def recomment_detail(request, parent_id, comment_id):
    parent_comment = Comment.objects.get(pk=parent_id)
    comment = Comment.objects.get(pk=comment_id)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(parent = parent_comment)
            return Response(serializer.data)

