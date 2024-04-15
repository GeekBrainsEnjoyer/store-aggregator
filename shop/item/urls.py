from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('new_item/', views.new_item, name='new_item')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
