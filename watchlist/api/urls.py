from django.urls import path
from watchlist.api.views import (WatchListAV, WatchDetails, StreamPlatformAV, 
                                 StreamPlatformDetail, ReviewList, ReviewDetail,
                                 ReviewCreate)

urlpatterns = [
     path('list/', WatchListAV.as_view(), name='watch-list'),
     path('<int:pk>/', WatchDetails.as_view(), name='watch-details'),
     path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
     path('stream/<int:pk>/', StreamPlatformDetail.as_view(), name='stream-details'),
     
     path("stream/<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"),
     path("stream/<int:pk>/review/", ReviewList.as_view(), name="review-list"),
     path("stream/review/<int:pk>", ReviewDetail.as_view(), name="review-details"),
    #  path('review/', ReviewList.as_view(), name='review-list'),
    #  path('review/<int:pk>/', ReviewDetail.as_view(), name='review-details'),
 ]
 