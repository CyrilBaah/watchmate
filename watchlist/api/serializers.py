from rest_framework import serializers
from watchlist.models import Movie


"""Validate length for movie name."""
def name_length(value):
    if len(value) < 5:
        raise serializers.ValidationError("Movie name is too short")
    


class MovieSerializer(serializers.Serializer):
    """Movie serializer"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    """Add a new movie to the list of movies"""
    def create (self, validate_data):
        return Movie.objects.create(**validate_data)
    
    """Update a movie to the list of movies"""
    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.description = validate_data.get('description', instance.description)
        instance.active = validate_data.get('activate', instance.active)
        instance.save()
        return instance
    
    """Validate different between name and description."""
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Movie name and description should be different")
        raise data