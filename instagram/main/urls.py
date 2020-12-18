from django.urls import path
from . import views


urlpatterns = [
    path('sign', views.signview),
    path('registration', views.registration),
    path('main', views.main_page),
]
