from app.models import Newsletter, Message

def get_object_by_id(id):
    obj = Newsletter.objects.get(pk=id)
    return obj

def delete_newsletter(newsletter):
    for msg in Message.objects.filter(newsletter=newsletter):
        msg.delete()
    newsletter.delete()