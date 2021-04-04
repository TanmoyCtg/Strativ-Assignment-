from django.db import models

# Create your models here.
class Post(models.Model):

    cname = models.CharField (max_length=255)
    alpha2Code = models.CharField(max_length=255)
    # timezone = models.TextField()
    capital = models.CharField(max_length=255)

    def __str__(self):
        return self.cname, self.alpha2Code, self.capital
class Test(models.Model):
    mydata = models.TextField()
