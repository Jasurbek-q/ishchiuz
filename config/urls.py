from django.urls import path
from . import views

urlpatterns = [
    path('',             views.home,   name='home'),
    path('ishchi/<int:pk>/', views.detail, name='detail'),
    path('elon/',        views.create, name='create'),
]