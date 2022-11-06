from rest_framework import serializers
from watchlist.models import Movie


class MovieSerializer(serializers.Serializer):
    """Movie serializer"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    def create (self, validate_data):
        return Movie.objects.create(**validate_data)