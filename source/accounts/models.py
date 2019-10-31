from django.contrib.auth.models import User
from django.db import models



class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    github = models.CharField(max_length=200,null=False, blank=True,verbose_name='Ссылка на гитхаб')

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

# Create your models here.
