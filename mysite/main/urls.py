from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("<int:id>", views.index, name='index'),
    path("", views.home,name='home'),
    path("home/", views.home,name='home'),
    path("create/", views.create,name='create'),
    path("view/", views.home,name='view'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    
]