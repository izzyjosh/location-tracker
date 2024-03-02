from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Location(models.Model):
    user:User = models.ForeignKey(User,on_delete=models.CASCADE)
    location:str = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location
