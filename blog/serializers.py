from rest_framework import serializers 
from .models import Post

class PostSerializers(serializers.ModelSerializer):

    class Meta:

        model = Post
        # need list of all countries 

        fields =['cname']

class CountrySpecific(serializers.ModelSerializer):

    class Meta:

        model = Post 
        
        fields = ['cname', 'alpha2Code', 'capital', 'population', 'timezone', 'flag', 'languages', 'borders']
