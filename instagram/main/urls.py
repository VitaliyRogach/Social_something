from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('sign', views.SignInView.as_view(), name='signin'),
    path('registration', views.SignUpView.as_view(), name='signup'),
    path('main', views.main_page, name='main'),
    path('logout', authViews.LogoutView.as_view(next_page='signin'), name='logout'),
    path('profile/', views.ProfileUser, name='profile')
]