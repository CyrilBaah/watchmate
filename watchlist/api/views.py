from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist.models import WatchList, StreamPlatform, Review
from watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from watchlist.api.permissions import IsAdminOrReadOnly, ReviewUserOrReadOnly


class WatchListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    """List all watchlist"""
    def get(self, request, *args, **kwargs):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response({ "data": serializer.data})
    
    """Create a new watchlist"""
    def post(self, request, *args, **kwargs):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ "data": serializer.data})
        else:
          return Response(serializer.errors)
      
      
class WatchDetails(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    """Get a single watchlist"""
    def get(self, request, pk, *args, **kwargs):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({ "Error": "Movie not found" })
        serializer = WatchListSerializer(movie)
        return Response( {"data": serializer.data} )
    
    """Update a watchlist"""
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( {"data": serializer.data} )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    """Delete a watchlist"""
    def delete(self, request, pk, *args, **kwargs):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class StreamPlatformAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    """List all streamplatforms"""
    def get(self, request, *args, **kwargs):
        streams = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streams, many=True)
        return Response( { "data": serializer.data} )
    
    """Create a new stream platform"""
    def post(self, request, *args, **kwargs):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( {"data": serializer.data} )
        else:
          return Response(serializer.errors)
      
      
class StreamPlatformDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    """Get a single stream platform"""
    def get(self, request, pk, *args, **kwargs):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({ "Error": "Movie not found", })
        serializer = StreamPlatformSerializer(stream)
        return Response({ "data": serializer.data })
    
    """Update a watchlist"""
    def put(self, request, pk):
        movie = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ "data": serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    """Delete a watchlist"""
    def delete(self, request, pk, *args, **kwargs):
        movie = StreamPlatform.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     """List all reviews"""
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     """Add a new review"""
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        return Review.objects.all()
    
    """Create a new review"""
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("You have already added a review")
        
        """Calculate the review rating"""
        if watchlist.number_rating == 0:
            watchlist.average_rating = serializer.validated_data['rating']
        else:
          watchlist.average_rating = (watchlist.average_rating + serializer.validated_data['rating']) / 2
          
        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()
        
        serializer.save(watchlist=watchlist, review_user=review_user)
     
class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer 
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAuthenticated]
    
    """Get specific review by id"""
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
        
class ReviewDetail(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [ReviewUserOrReadOnly]
    
    
    # """Get a single review"""
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    
    