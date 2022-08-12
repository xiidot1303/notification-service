from datetime import datetime
from app.models import *
from app.utils import send_request

def create_messages(newsletter):
    now = datetime.now()
    for client in Client.objects.filter(tag=newsletter.client_property['tag'], code=newsletter.client_property['code']):
        message = Message.objects.create(
            status = 'waiting',
            newsletter = newsletter,
            client = client
        )
    if now >= newsletter.start_time.replace(tzinfo=None) and now <= newsletter.end_time.replace(tzinfo=None):
        send_message(message)
    
def edit_messages(newsletter):
    is_changed_client = False
    for msg in Message.objects.filter(newsletter=newsletter, status='waiting'):
        if msg.client.code != newsletter.client_property['code'] or msg.client.tag != newsletter.client_property['tag']:
            msg.delete()
            is_changed_client = True
    else:
        is_changed_client = True
    if is_changed_client:
        create_messages(newsletter)


def send_message(message):
    now = datetime.now()
    data = {
        'id': message.id,
        'phone': message.client.phone,
        'text': message.newsletter.message_text
    }
    request = send_request.send_message(data=data, msg_id=message.id)
    if request:
        message.create_time = now
        message.status = 'sent'
        message.save()