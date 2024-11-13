from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer


# Create your views here.
@api_view(['GET'])
def get_user(request):
    # users = User.objects.all()
    # serializer = UserSerializer(users, many=True)
    # return Response(serializer.data)
    return Response(
        UserSerializer(
            {
                "name": "John Doe",
                "age": 30,
                "email": "john.doe@example.com",
                "password": "securepassword123",
            }
        ).data, status=status.HTTP_200_OK
    )
