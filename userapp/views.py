from rest_framework.decorators import api_view
from rest_framework.response import Response
from userapp.serializers import RegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
@api_view(['POST'])
def registration_view(request):
    """Register a User"""
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        # return Response(serializer.initial_data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registeration successful"
            data['username'] = account.username
            data['email'] = account.email


            refresh = RefreshToken.for_user(account)
            data['token'] = {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                            }
        else:
          data = serializer.errors
        return Response(data)
        # return Response(request.data)
        # serializer = RegistrationSerializer(data=request.data)  
        # return Response(serializer.is_valid()) 
           
        # return Response(serializer.initial_data) 
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data)
            # return Response(serializer.data)