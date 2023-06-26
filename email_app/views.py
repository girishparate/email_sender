from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from .serializers import EmailCredentialSerializer, MailSerializer, EmailCredential, Mail, MailTracker
from django.views.generic import DetailView
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import EmailMultiAlternatives
from django.utils.text import slugify
from django.contrib.sites.shortcuts import get_current_site
from datetime import datetime
from django.contrib import messages 


# Create your views here.
class MainDashboard(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main_dashboard.html'

    def get(self, request):
        mail_list = Mail.objects.filter(sender=request.user).order_by('id')[::-1]
        data = {'mail_list':mail_list}
        if EmailCredential.objects.filter(email_owner=request.user).exists():
            email_credentials = EmailCredential.objects.get(email_owner=request.user)
            data['email_credentials'] = email_credentials
        return Response(data)
    
class EmailCredentialSettingView(APIView):
    def post(self, request):
        data = {}
        serializer = EmailCredentialSerializer(data=request.data)

        if serializer.is_valid():
            encoded_password = urlsafe_base64_encode(force_bytes(request.data['email_password']))
            serializer.save(email_owner=request.user, email_password=encoded_password)
            messages.success(request, "Email credentials saved.")
            data['message'] = 'Email credentials saved.'
        else:
            messages.error(request, "Could not save email credentials.")
            data['message'] = 'Could not save email credentials.'
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
class UpdateEmailCredentialView(APIView):
    def put(self, request):
        data = {}
        email_object = EmailCredential.objects.get(email_owner=request.user)
        serializer = EmailCredentialSerializer(instance=email_object, data=request.data)
        if serializer.is_valid():
            encoded_password = urlsafe_base64_encode(force_bytes(request.data['email_password']))
            serializer.save(email_owner=request.user, email_password=encoded_password)
            messages.success(request, "Email credentials updated.")
            data['message'] = 'Email credentials updated.'
        else:
            messages.error(request, "Could not update email credentials.")
            data['message'] = 'Could not save update credentials.'
        return Response(data)
    
class SendEmailView(APIView):
    def post(self, request):
        data = {}

        serializer = MailSerializer(data=request.data)
        if serializer.is_valid():
            saved_serializer = serializer.save(sender=request.user, sent_time=datetime.now())
            saved_serializer.slug = slugify(request.data['subject']+' '+str(saved_serializer.id))
            saved_serializer.save()
            email_credential = EmailCredential.objects.get(email_owner=request.user)
            decoded_password = urlsafe_base64_decode(email_credential.email_password).decode()
            current_site = get_current_site(request).domain
            encoded_mail_id = urlsafe_base64_encode(force_bytes(saved_serializer.id))

            message = render_to_string('mail_template.html', {
                                                        'domain': current_site,
                                                        'uid': encoded_mail_id,
                                                        'messsage': saved_serializer.body,
                                                        'mail_section': 'mail-status',
                                                })
        
            backend = EmailBackend(host=email_credential.smtp_provider, port=email_credential.port, username=email_credential.email, password=decoded_password, use_tls=True, fail_silently=False)

            msg = EmailMultiAlternatives(subject=saved_serializer.subject, body=message, from_email=email_credential.email, to=[saved_serializer.receiver], connection=backend)
            
            msg.content_subtype = 'html'
            msg.send()
            messages.success(request, "Email sent successfully.")
            data['message'] = 'Email sent successfully.'
        else:
            messages.error(request, "Could not sent mail.")
            data['message'] = 'Could not sent mail.'
            
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
class EmailDetailView(DetailView):
    model = Mail
    template_name = 'mail_detail.html'

class MailStatusView(APIView):
    def get(self, request, uidb64):
        id = urlsafe_base64_decode(uidb64).decode()
        send_mail = Mail.objects.get(pk=id)
        send_mail.status = True
        send_mail.save()
        MailTracker.objects.create(mail=send_mail, read_time = datetime.now()).save()
        data = None
        return Response(data)