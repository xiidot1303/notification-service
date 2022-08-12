from app.models import Message
from app.services.messageservice import send_message
from datetime import datetime

def check_messages():
    print('\n\nJOB\n\n')
    now = datetime.now()
    for msg in Message.objects.filter(status='waiting'):
        if now >= msg.newsletter.start_time.replace(tzinfo=None) and now <= msg.newsletter.end_time.replace(tzinfo=None):
            send_message(msg)
        elif now > msg.newsletter.end_time.replace(tzinfo=None):
            # deadline ended
            msg.delete()