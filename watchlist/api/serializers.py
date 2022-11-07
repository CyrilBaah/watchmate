from rest_framework import serializers
from watchlist.models import Movie


class MovieSerializer(serializers.Serializer):
    """Movie serializer"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    """Add a new movie to the list of movies"""
    def create (self, validate_data):
        return Movie.objects.create(**validate_data)
    
    """Update a movie to the list of movies"""
    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.description = validate_data.get('description', instance.description)
        instance.activate = validate_data.get('activate', instance.activate)
        instance.save()
        return instance