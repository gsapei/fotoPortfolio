from turtle import home
from django.contrib import admin
from django.urls import path
from portfolio import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name="about"),
    path('', views.home, name='home'),
    path("foto/<int:foto_id>", views.detalle_foto, name='detalle_foto')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)