from django.urls import path
from watchlist.api.views import MovieList, MovieDetails

urlpatterns = [
     path('list/', MovieList.as_view(), name='movie-list'),
     path('<int:pk>/', MovieDetails.as_view(), name='movie-details'),
 ]
 