from django.contrib.auth.models import User
from django.db import models



class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    github = models.URLField(max_length=200,null=True, blank=True,verbose_name='Ссылка на гитхаб')
    about = models.TextField(max_length=2000,null=True, blank=True, verbose_name='О себе ')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    def __str__(self):
        return self.user
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'




# Create your models here.
