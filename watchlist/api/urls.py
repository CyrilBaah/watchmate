from django.urls import path
from watchlist.api.views import WatchListAV, WatchDetails, StreamPlatformAV, StreamPlatformDetail

urlpatterns = [
     path('list/', WatchListAV.as_view(), name='watch-list'),
     path('<int:pk>/', WatchDetails.as_view(), name='watch-details'),
     path('streams/', StreamPlatformAV.as_view(), name="stream-list"),
     path('streams/<int:pk>/', StreamPlatformDetail.as_view())
 ]
 