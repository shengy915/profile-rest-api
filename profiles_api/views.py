from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions
class HelloApiView(APIView):
    """test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns list of APIView features"""
        an_apiview = [
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'gives you most control over your application logic',
            'is mapped manually to urls',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """create a hello msg w our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
                )
    #pk = primary key = id of obj to update
    #replaces obj
    def put(self, request, pk = None):
        """handle updating obj"""
        return Response({'method':'PUT'})
    #only update fields requested to be updated, not all fields
    def patch(self, request, pk = None):
        """Handle partial update of obj"""
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk = None):
        """delete an obj"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello msg"""
        a_viewset = [
            'uses actions (list, create, retrieve, update, partial_update)',
            'automatically maps to urls using routers',
            'provides more functionality with less code',
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """create a new hello msg"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
                )
        
    def retrieve(self, request, pk=None):
        """handle getting an obj by its ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """handle updating an obj"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """handle partial updating of an obj"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """handle deleting an obj"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)