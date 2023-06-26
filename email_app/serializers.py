from rest_framework.serializers import ModelSerializer
from .models import EmailCredential, Mail, MailTracker

class EmailCredentialSerializer(ModelSerializer):
    class Meta:
        model = EmailCredential
        exclude = ['email_owner']

class MailSerializer(ModelSerializer):
    class Meta:
        model = Mail
        exclude = ['sender', 'status', 'sent_time', 'slug']
