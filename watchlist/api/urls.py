from django.urls import path
from watchlist.api.views import WatchListAV, WatchDetails, StreamPlatformList

urlpatterns = [
     path('list/', WatchListAV.as_view(), name='watch-list'),
     path('<int:pk>/', WatchDetails.as_view(), name='watch-details'),
     path('streams/', StreamPlatformList.as_view(), name="stream-list"),
 ]
 