from django.db import models

# Create your models here.
class Post(models.Model):

    cname = models.CharField (max_length=255)
    alpha2Code = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    population = models.CharField(max_length=255)
    timezone = models.TextField()
    flag = models.URLField()
    languages = models.TextField()
    borders = models.TextField()

    def __str__(self):
        return '%s %s %s %s %s %s %s %s' %(self.cname, self.alpha2Code, self.capital, self.population, self.timezone, self.flag, self.languages, self.borders)


