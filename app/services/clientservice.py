from app.models import Message, Client, Newsletter
from django.db.models import Count
from app.services import newsletterservice

def get_object_by_id(id):
    return Client.objects.get(pk=id)

def delete_client(client):
    for msg in Message.objects.filter(client=client):
        msg.delete()
    client.delete()


def add_client_to_messages(client):
    messages = Message.objects.filter(
        newsletter__client_property__code = client.code, 
        newsletter__client_property__tag = client.tag,
        status = 'waiting'
    ).values('newsletter').annotate(c=Count('newsletter'))
    for msg in messages:
        newsletter = newsletterservice.get_object_by_id(msg['newsletter'])
        Message.objects.create(
            status = 'waiting',
            newsletter = newsletter,
            client = client
        )


def check_filter(client):
    for msg in Message.objects.filter(status='waiting', client=client):
        if not is_filter_same(msg, client):
            msg.delete()
            add_client_to_messages(client)

def is_filter_same(message, client):
    if (str(message.newsletter.client_property['code']) == client.code 
    and str(message.newsletter.client_property['tag']) == client.tag):
        return True
    return False