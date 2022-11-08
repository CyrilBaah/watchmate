from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def movie_list(request):
    """Get all movies"""
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    """Create a new movie"""
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
          return Response(serializer._errors)
      
      
@api_view(['GET', 'POST', 'DELETE'])
def movie_details(request, pk):
    """Get a single movie details"""
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({ "Error": "Movie not found" })
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    """Update a movie details"""
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    """Delete a movie details"""
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
