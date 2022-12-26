from rest_framework import serializers
from .models import Movie, Genre, Review, Moviecup

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']
        
class MovieSerializer(serializers.ModelSerializer):        
    genres = GenreSerializer(many=True)
    class Meta :
        model = Movie
        fields = '__all__'
        read_only_fields = ('user', 'like_users',)

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)  
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie','like_users',)