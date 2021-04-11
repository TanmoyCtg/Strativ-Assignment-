from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
from . models import Post
from rest_framework.views import APIView
from . serializers import PostSerializers, CountrySpecific
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q
from django.views.generic import ListView, TemplateView
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# this api returns list of all countries name

class CountryList(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]   

    def get(self, request):
        countrylist = Post.objects.all()
        serializer = PostSerializers(countrylist, many = True)
        
        return Response (serializer.data)

# Details of an specific country

class getCountry(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        specific_country_list = Post.objects.get(pk=1)
        serializer = CountrySpecific(specific_country_list)
        return Response(serializer.data)



# creating a new country and added all information
# new country Bangladesh
class CreatingNewCountry(generics.ListCreateAPIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = CountrySpecific

# update an existing country
#  I updated the country Albania to ALBANIA
# using this api also we can delete any country information

class updateDeleteCountry(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = CountrySpecific

# class searchCountry(APIView):
#     def get(self, request):

#         queryset = Post.objects.raw("select id,cname from blog_post where cname")
#         for i in queryset:
#             print(i.cname)
#         serializer = searchCountrySerializer(queryset)

#         return Response(serializer.data)
    
    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = CountrySpecific(list(queryset), many=True)
    #     return Response(serializer.data)


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




# search country and see the details 
class HomePageView(TemplateView):
    template_name = 'blog/country.html'

class SearchResultsView(ListView):

    model = Post 
    template_name = 'blog/searchform.html'

    def get_queryset(self):

        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(cname__icontains=query))

        return object_list
        
        
 


    

