from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages


# Create your views here.
class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        return Response(data={})
    
    def post(self, request):
        if User.objects.filter(email=request.data['email']).exists():
            user = User.objects.get(email=request.data['email'])
            correct_password = check_password(request.data['password'], user.password)
            if correct_password:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Wrong password.")
                return Response(data={'message':'Wrong password.'})    
        else:
            messages.error(request, "Email does not exists.")
            return Response(data={'message':'Email does not exists.'})
    

class Registration(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration.html'

    def get(self, request):
        return Response(data={})
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        hashed_password = make_password(password)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email address already registered.")
        else:
            user = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=email, password=hashed_password)
            user.save()
            login(request, user)
            messages.success(request, "Congratulation! You have successfully register.")
        return redirect('/')
    
class Logout(APIView):
    def get(self, request):
        logout(request)
        return redirect('/')
    