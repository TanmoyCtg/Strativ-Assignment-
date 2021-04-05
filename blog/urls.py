from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('country/', views.CountryList.as_view())
]