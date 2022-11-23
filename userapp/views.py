from rest_framework.decorators import api_view
from rest_framework.response import Response
from userapp.serializers import RegistrationSerializer

# Create your views here.
@api_view(['POST'])
def registration_view(request):
    """Register a User"""
    if request.method == 'POST':
        # return Response(request.data)
        serializer = RegistrationSerializer(data=request.data)  
        return Response(serializer.is_valid()) 
           
        # return Response(serializer.initial_data) 
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data)
            # return Response(serializer.data)