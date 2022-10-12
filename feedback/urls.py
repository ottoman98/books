from django.urls import path
from . import views

urlpatterns = [
    path('contactanos/', views.Contactanos, name='contactanos'),

]