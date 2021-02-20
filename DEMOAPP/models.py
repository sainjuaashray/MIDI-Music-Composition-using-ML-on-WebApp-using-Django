from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#class Post(models.Model):
#    title = models.CharField(max_length = 100)
#    content = models.TextField()
#    date_posted = models.DateTimeField(default = timezone.now)
##    auth = models.ForeignKey(User, on_delete=models.CASCADE)

#class Hobby(models.Model):
#    name = models.ForeignKey(User, on_delete=models.CASCADE)
#    hobby1 = models.CharField(max_length=25)
#    hobby2 = models.CharField(max_length=25)