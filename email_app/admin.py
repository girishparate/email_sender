from django.contrib import admin
from .models import EmailCredential, Mail

# Register your models here.
admin.site.register(EmailCredential)
admin.site.register(Mail)