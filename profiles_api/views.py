from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns list of APIView features"""
        an_apiview = [
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'is similat rp traditional django view',
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
        
    def put(self, request, pk = None):
        """handle updating obj"""
        return Response({'method':'PUT'})
    
    def patch(self, request, pk = None):
        """Handle partial update of obj"""
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk = None):
        """delete an obj"""
        return Response({'method':'DELETE'})