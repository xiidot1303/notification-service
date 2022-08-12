from django.db import models
import pytz

class Newsletter(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    message_text = models.TextField(null=True, blank=True, max_length=5000)
    end_time = models.DateTimeField(null=True, blank=True)
    client_property = models.JSONField(null=True, blank=True)
    # client = models.ForeignKey('Client', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return '{}: {}, {}'.format(
            self.pk,
            self.client_property['code'],
            self.client_property['tag']
        )

class Client(models.Model):
    TIMEZONES = tuple(
        zip(
            pytz.all_timezones, 
            pytz.all_timezones
            )
    )
    
    phone = models.CharField(null=True, blank=True, max_length=16)
    code = models.CharField(null=True, blank=True, max_length=16)
    tag = models.CharField(null=True, blank=True, max_length=255)
    timezone = models.CharField(null=True, blank=True, max_length=100, choices=TIMEZONES)

    def __str__(self) -> str:
        return '{}: {}, {}'.format(
            self.pk,
            self.code,
            self.tag
        )

class Message(models.Model):
    create_time = models.DateTimeField(null=True, blank=True)
    STATUS = (
        ('sent', 'Отправлено'),
        ('waiting', 'В ожидании')
    )
    status = models.CharField(null=True, blank=True, max_length=50, choices=STATUS)
    newsletter = models.ForeignKey('Newsletter', null=True, blank=True, on_delete=models.PROTECT)
    client = models.ForeignKey('Client', null=True, blank=True, on_delete=models.PROTECT)

    