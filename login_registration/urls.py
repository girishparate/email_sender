from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('login', Login.as_view(), name='login'),

    path('registration', Registration.as_view(), name='registration'),

    path('logout', login_required(Logout.as_view()), name='logout')
]