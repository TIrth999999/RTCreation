from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('review/', views.review, name='review'),
    path('contact/', views.contact, name='contact'),
]