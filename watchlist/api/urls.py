from django.urls import path
from watchlist.api.views import WatchListAV, WatchDetails, StreamPlatformAV, StreamPlatformDetail, ReviewList

urlpatterns = [
     path('list/', WatchListAV.as_view(), name='watch-list'),
     path('<int:pk>/', WatchDetails.as_view(), name='watch-details'),
     path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
     path('stream/<int:pk>/', StreamPlatformDetail.as_view(), name='stream-details'),
     path('review/', ReviewList.as_view(), name='review-list'),
 ]
 