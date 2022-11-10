from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist.models import WatchList, StreamPlatform
from watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer
from rest_framework import status


class WatchListAV(APIView):
    """List all watchlist"""
    def get(self, request, *args, **kwargs):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    """Create a new watchlist"""
    def post(self, request, *args, **kwargs):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
          return Response(serializer._errors)
      
      
class WatchDetails(APIView):
    """Get a single watchlist"""
    def get(self, request, pk, *args, **kwargs):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({ "Error": "Movie not found" })
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    """Update a watchlist"""
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    """Delete a watchlist"""
    def delete(self, request, pk, *args, **kwargs):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class StreamPlatformAV(APIView):
    """List all streamplatforms"""
    def get(self, request, *args, **kwargs):
        streams = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streams, many=True)
        return Response(serializer.data)
    
    """Create a new stream platform"""
    def post(self, request, *args, **kwargs):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
          return Response(serializer._errors)
      
      
class StreamPlatformDetail(APIView):
    """Get a single stream platform"""
    def get(self, request, pk, *args, **kwargs):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({ "Error": "Movie not found" })
        serializer = StreamPlatformSerializer(stream)
        return Response(serializer.data)
    
    """Update a watchlist"""
    def put(self, request, pk):
        movie = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    """Delete a watchlist"""
    def delete(self, request, pk, *args, **kwargs):
        movie = StreamPlatform.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)