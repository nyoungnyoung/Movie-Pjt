from rest_framework import serializers
from .models import User, Guestbook


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('followings',)


class GuestbookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Guestbook
        fields = '__all__'
        read_only_fields = ('from_user','to_user')