from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers')
    introduction = models.TextField(null=True, blank=True, default="안녕하세요! 반갑습니다😘")
    name = models.CharField(max_length=20, null=True, blank=True)
    profile_image = models.ImageField(upload_to='uploads', blank=True, null=True)
    
    def __str__(self):
        return self.username

class Guestbook(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "write_books")
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "receive_books")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
