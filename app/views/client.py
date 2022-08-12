from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.models import *
from app.serializers import *
from app.services import clientservice as cls

@api_view(['POST', 'GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def client_create(request):
    # Create object
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            client_obj = cls.get_object_by_id(serializer.data.get('id'))
            cls.add_client_to_messages(client_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def client_edit(request, pk):
    client = cls.get_object_by_id(pk)
    
    # Check request method.
    if request.method == 'DELETE':
        cls.delete_client(client)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # Change object
    serializer = ClientSerializer(client, data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            cls.check_filter(client)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
