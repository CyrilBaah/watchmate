from rest_framework import serializers
from watchlist.models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
    # length_of_name  = serializers.SerializerMethodField()
    class Meta:
      model = WatchList
      fields = "__all__"
      
      
class StreamPlatformSerializer(serializers.ModelSerializer):
  class Meta:
    model = StreamPlatform
    fields = "__all__"
      
    # """Get length of movie name."""
    # def get_length_of_name(self, object):
    #     return len(object.name)     
      
    # """Validate different between name and description."""
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Movie name and description should be different")
    #     return data
    
    # """Validate length for movie name."""
    # def validate_name(self, value):
    #     if len(value) < 5:
    #         raise serializers.ValidationError("Movie name is too short")
    #     else:
    #       return value
