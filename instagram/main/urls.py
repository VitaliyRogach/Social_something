from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('sing', views.singview),

]
