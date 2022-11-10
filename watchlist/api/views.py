from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist.models import WatchList
from watchlist.api.serializers import WatchListSerializer
from rest_framework import status


class MovieList(APIView):
    """List all movies"""
    def get(self, request, *args, **kwargs):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    """Create a new movie"""
    def post(self, request, *args, **kwargs):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
          return Response(serializer._errors)
      
      
class MovieDetails(APIView):
    """Get a single Movie"""
    def get(self, request, pk, *args, **kwargs):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({ "Error": "Movie not found" })
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    """Update a movie"""
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    """Delete a movie"""
    def delete(self, request, pk, *args, **kwargs):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
