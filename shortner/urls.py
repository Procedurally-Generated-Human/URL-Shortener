from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('<str:shrt_url>/', views.redirect_to_link, name="redirect_to_link"),
]