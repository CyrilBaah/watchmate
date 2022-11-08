from django.urls import path
from watchlist.api.views import MovieList, movie_details

urlpatterns = [
     path('list/', MovieList.as_view(), name='movie-list'),
     path('<int:pk>/', movie_details, name='movie-details'),
 ]
 