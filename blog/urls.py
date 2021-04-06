from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('country/', views.CountryList.as_view()),
    path('country/1/' , views.getCountry.as_view()),
    path('country/add/', views.CreatingNewCountry.as_view())
]