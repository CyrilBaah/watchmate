from django.urls import path
from watchlist.api.views import WatchList, WatchDetails

urlpatterns = [
     path('list/', WatchList.as_view(), name='movie-list'),
     path('<int:pk>/', WatchDetails.as_view(), name='movie-details'),
 ]
 