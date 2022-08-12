from django.contrib import admin
from app.models import *
from rest_framework.authtoken.models import Token

class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'phone', 'code', 'tag', 'timezone')

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client_property', 'start_time', 'end_time')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('create_time', 'status', 'newsletter', 'client')

class TokenAdmin(admin.ModelAdmin):
    list_display = ()

admin.site.register(Client, ClientAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Message, MessageAdmin)
# admin.site.register(Token, TokenAdmin)

