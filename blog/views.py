from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
from .models import Post
posts= [
    {
        "name":"Afghanistan",
        "alpha2Code":"AF",
        "timezones":["UTC+01:00"],
        "borders":["MNE","GRC","MKD","KOS"],
        "capital":"Kabul"
    },
    {
        "name":"Albania",
        "alpha2Code":"GE",
        "timezones":["UTC+01:00"],
        "borders":["MNE","GRC","MKD","KOS"],
        "capital":"Kabul"
        
    }
        
]
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
        post = Post(cname=name, alpha2Code=alpha2Code, capital=capital)
        post.save()
    return render(request, 'blog/data.html',context)


def about(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context )
        