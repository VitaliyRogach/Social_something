from django.urls import path
from . import views


urlpatterns = [
    path('sign', views.SignInView.as_view(), name='signin'),
    path('registration', views.SignUpView.as_view(), name='signup'),
    path('main', views.main_page, name='main'),
]