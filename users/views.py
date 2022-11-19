from django.http import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer

# Create your views here.

class UsersApiView(APIView):

  permission_classes = [permissions.IsAdminUser]

  def get(self, request, *args, **kwargs):
    """
    View all users listed in the system
    """

    usernames = [user.name for user in User.objects.all()]
    return Response(usernames)

class UserApiView(ViewSet):

  permission_classes = [permissions.IsAuthenticated]

  def get_object(self, pk):
    """
    Get a single user in the system 
    """
    try:
      return User.objects.get(pk=pk)
    except User.DoesNotExist:
      raise Http404


  def get(self, request, pk): 

    user = self.get_object(pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


  def post(self, request):
    """
    Creates a new user in the system. 
    """
    user = { 'name': request.data.get('name'),
             'description': request.data.get('description'),
             'email': request.data.get('email'),
             'phone': request.data.get('phone')
             }
    serializer = UserSerializer(data=user)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
