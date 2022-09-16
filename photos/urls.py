from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Galeria, name='galeria'),
    path('foto/<str:pk>/', views.VerFoto, name='foto'),
    path('agregar/', views.AgregarFoto, name='agregar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
