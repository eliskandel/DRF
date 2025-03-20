from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User

class Platform(models.Model):
    name= models.CharField(max_length=100)
    detail=models.CharField(max_length=200)
    website=models.URLField(max_length=200)

    def __str__(self):
        return self.name
    
    
class WatchList(models.Model):
    title= models.CharField(max_length=50)
    storyline= models.CharField(max_length=200)
    platform=models.ForeignKey(Platform,on_delete=models.CASCADE, related_name="watchlist")
    active=models.BooleanField(default=True)
    created=models.DateField()

    def __str__(self):
        return self.title

class Review(models.Model):
    review_user= models.ForeignKey(User, on_delete=models.CASCADE)
    rating= models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description= models.CharField(max_length=100, null=True)
    watchlist=models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="review")
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)+self.watchlist.title