from django.urls import path
from django.contrib.auth import views as auth_view
from django.contrib.auth.forms import AuthenticationForm

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name='core/login.html',
         authentication_form=AuthenticationForm), name='login')
]
