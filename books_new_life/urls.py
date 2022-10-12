from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('books.urls')),
    path("about/", views.about, name="about"),
    path("miembros/", include('django.contrib.auth.urls')),
    path("miembros/", include('miembros.urls')),
    path("", include('feedback.urls')),
    path("politicas/", views.politicas, name="politicas"),
    path("tratamientodatos/", views.tratamientoDatos, name="tratamientoDatos"),
    path("guia/", views.guiaUser, name="guiaUser"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
