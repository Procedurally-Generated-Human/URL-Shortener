from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('create/<int:id>/', views.create, name="create"),
]