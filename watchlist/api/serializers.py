from rest_framework import serializers
from watchlist.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = "__all__"    

class WatchListSerializer(serializers.ModelSerializer):
  reviews = ReviewSerializer(many=True, read_only=True)
  class Meta:
    model = WatchList
    exclude = ('watchlist', )
    # fields = "__all__"
      
      
class StreamPlatformSerializer(serializers.ModelSerializer):
  watchlist = WatchListSerializer(many=True, read_only=True)
  class Meta:
    model = StreamPlatform
    fields = "__all__"
      