from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class Category(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.username



class Info(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='')
    link = models.URLField()
    description = models.CharField(max_length=1000, default='')



def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = Category.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender= User)




