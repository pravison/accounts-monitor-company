from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact', views.contactMessage, name='contact'),
    path('newsletter', views.NewsLetter, name='newsletter')
]