from rest_framework import serializers
from app.models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'phone', 'code', 'tag', 'timezone']

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id', 'start_time', 'message_text', 'end_time', 'client_property']