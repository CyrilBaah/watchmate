from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    """Movie serializer"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    # def create (self, validate_data):
    #     Mo