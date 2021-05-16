from django.urls import path
from . import views
from .views import contactView, successView, homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('registry', contactView, name='registry'),
    path('success/', successView, name='success'),
]