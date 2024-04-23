from django.urls import path
from app import views

urlpatterns = [
    path("", views.index),
    path('formulario/', views.form_user_view, name='form_user'),
    path('tabla/', views.tabla, name='tabla' ),
    path('acerca/', views.acerca, name='acerca' ),
    path('seguns/', views.seg, name='proceso' ),
]

