from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count
from app.models import *
from app.serializers import *
from app.services import messageservice as msgs
from app.services import newsletterservice as nls


@api_view(['POST', 'GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def newsletter_create(request):
    # Create object
    serializer = NewsletterSerializer(data=request.data)
    if serializer.is_valid():
        if True:
        # try:
            serializer.save()
            newsletter_obj = nls.get_object_by_id(serializer.data.get('id'))
            msgs.create_messages(newsletter_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # except:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def newsletter_edit(request, pk):
    newsletter = nls.get_object_by_id(pk)

    # Check request method. Delete object if method is DELETE
    if request.method == 'DELETE':
        nls.delete_newsletter(newsletter)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # Change object
    serializer = NewsletterSerializer(newsletter, data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            msgs.edit_messages(newsletter)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def newsletter_overall_statistics(request):
    result = []
    newsletters = Newsletter.objects.all()
    for obj in newsletters:
        messages = list(
            Message.objects.filter(newsletter__pk=obj.pk).values('status').annotate(
                status_c=Count('status')
                    ).values_list('status', 'status_c')
        )
        messages_count_by_status = {i[0]: i[1] for i in messages}
        messages_count = {'all': len(Message.objects.filter(newsletter__pk=obj.pk))}
        messages_count.update(messages_count_by_status)
        newsletter_info = {
            'id': obj.pk,
            'start_time': obj.start_time,
            'message_text': obj.message_text,
            'client_property': obj.client_property,
            'messages': messages_count
        }
        result.append(newsletter_info)


    return Response(result, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def newsletter_statistic(request, pk):
    newsletter = nls.get_object_by_id(pk)
    messages = []
    for m in Message.objects.filter(newsletter = newsletter):
        info = {
            'create_time': m.create_time,
            'status': m.status,
            'client': m.client.pk
        }
        messages.append(info)

    newsletter_info = {
        'id': newsletter.pk,
        'start_time': newsletter.start_time,
        'message_text': newsletter.message_text,
        'client_property': newsletter.client_property,
        'messages': messages 
    }

    return Response(newsletter_info, status=status.HTTP_200_OK)
