from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=200, default="")
    category = models.CharField(max_length=200, default="Movie")
    genres = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=1500, default="")
    trailer = models.CharField(max_length=300, default="")
    rate = models.CharField(max_length=300, default="")
    collection = models.CharField(max_length=300, default="")
    views = models.IntegerField(default=0)
    imgurl = models.CharField(max_length=1000, default="")
    bigimgurl = models.CharField(max_length=1000, default="")
    vidurl = models.CharField(max_length=1000, default="", blank=True)
    suburl = models.CharField(max_length=1000, default="", blank=True)

    def __str__(self):
        return self.name


class Tvshows(models.Model):
    name = models.CharField(max_length=200, default="")
    category = models.CharField(max_length=200, default="Tv Serie")
    genres = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=1500, default="")
    trailer = models.CharField(max_length=300, default="")
    rate = models.CharField(max_length=300, default="")
    number_season = models.IntegerField(default=0)
    imgurl = models.CharField(max_length=1000, default="")
    bigimgurl = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name


class Episodes(models.Model):
    name = models.CharField(max_length=200, default="")
    seasons = models.IntegerField(default=0)
    episodes = models.IntegerField(default=0)
    title = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=1000, default="")
    imgurl = models.CharField(max_length=1000, default="")
    vidurl = models.CharField(max_length=1000, default="", blank=True)
    suburl = models.CharField(max_length=1000, default="", blank=True)

    def __str__(self):
        return self.name + " Season " + str(self.seasons) + " Episode " + str(self.episodes)


class Comingsoon(models.Model):
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    imgurl = models.CharField(max_length=300)

    def __str__(self):
        return self.name
