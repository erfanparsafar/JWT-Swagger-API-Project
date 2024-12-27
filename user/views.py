from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , permissions
from drf_spectacular.utils import extend_schema
from .serializers import RegisterSerializer , ProfileSerializer

# Create your views here.
extend_schema(
    tags = ['Authentications']
    
)
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(responses= RegisterSerializer)
    def get(self,request):
        serializer = RegisterSerializer ()
        return Response(serializer.data , status = status.HTTP_200_OK)
    
    @extend_schema(request=RegisterSerializer, responses=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(RegisterSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    @extend_schema(responses= ProfileSerializer)
    def get(self,request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data , status = status.HTTP_200_OK)
    