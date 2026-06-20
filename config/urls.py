from django.urls import path
from . import views

urlpatterns = [
    path("", views.kirish, name="kirish"),
    path("royxat/", views.foydalanuvchi_create, name="foydalanuvchi_create"),
    path('chiqish/',  views.chiqish,         name='chiqish'),
    path("foydalanuvchi/detail/", views.foydalanuvchi_detail, name="foydalanuvchi_detail"),
    path("foydalanuvchi/list/", views.foydalanuvchi_list, name="foydalanuvchi_list"),
    path('home/',             views.home,   name='home'),
    path('ishchi/<int:pk>/', views.detail, name='detail'),
    path('elon/',        views.create, name='create'),
]