from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmailCredential(models.Model):
    email_owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    smtp_provider = models.CharField(max_length=200, help_text='Enter smtp service provider')
    port = models.SmallIntegerField(default=587)
    email = models.EmailField()
    email_password = models.CharField(max_length=200, help_text='Enter email password')
    email_use_tls = models.BooleanField(default=True)

    def __str__(self):
        return str(self.email_owner)
    

class Mail(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.EmailField()
    subject = models.CharField(max_length=1000)
    body = models.TextField()
    status = models.BooleanField(default=False)
    sent_time = models.DateTimeField()
    slug = models.SlugField()
    
    def __str__(self):
        return str(self.subject)
    
class MailTracker(models.Model):
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE)
    read_time = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.mail)