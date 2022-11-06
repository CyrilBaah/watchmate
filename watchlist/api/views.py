from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer


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