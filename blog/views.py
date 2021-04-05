from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
from . models import Post
from rest_framework.views import APIView
from . serializers import PostSerializers
from rest_framework.response import Response 

class CountryList(APIView):

    def get(self, request):
        countrylist = Post.objects.all()
        serializer = PostSerializers(countrylist, many = True)
        return Response (serializer.data)


def home(request):
    url = 'https://restcountries.eu/rest/v2/all'
    response = requests.get(url)
    data = response.json()
    context = {

        'data': data 
    }

    for d in data:

        name = d.get('name')
        alpha2Code = d.get('alpha2Code')
        capital = d.get('capital')
        population = d.get('population')
        timezone = d.get('timezones')
        flag = d.get('flag')
        languages = d.get('languages')
        borders = d.get('borders')

        post = Post(cname=name, alpha2Code=alpha2Code, capital=capital, population=population, timezone=timezone, flag=flag, languages=languages, borders=borders)
        post.save()
    
    return render(request, 'blog/data.html',context)



        