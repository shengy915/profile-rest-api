from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """test API view"""

    def get(self, request, format=None):
        """returns list of APIView features"""
        an_apiview = [
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'is similat rp traditional django view',
            'gives you most control over your application logic',
            'is mapped manually to urls',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})