from django.urls import path
from django.contrib.auth import views as auth_view
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name='core/login.html',
         authentication_form=LoginForm), name='login'),
    path('accounts/logout/',
         auth_view.LogoutView.as_view(template_name="core/index.html"), name='logout')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
