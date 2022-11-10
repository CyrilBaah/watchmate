from rest_framework import serializers
from watchlist.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
      model = Movie
      fields = "__all__"
      
      
    """Validate different between name and description."""
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Movie name and description should be different")
        return data
    
    """Validate length for movie name."""
    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Movie name is too short")
        else:
          return value
