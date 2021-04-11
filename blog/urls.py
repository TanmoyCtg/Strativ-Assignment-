from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('country/', views.CountryList.as_view()),
    path('country/1/' , views.getCountry.as_view()),
    path('country/add/', views.CreatingNewCountry.as_view()),
    path('country/update/<int:pk>/', views.updateDeleteCountry.as_view()),
    
    path('country/search/', views.SearchResultsView.as_view(), name='search'),
    path('countrypage/', views.HomePageView.as_view(), name='countrypage'),
]