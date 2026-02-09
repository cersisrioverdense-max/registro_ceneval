from django.urls import path
from .views import redireccion_post_login, datos_personales, bloque2, bloque3, bloque4, registro_finalizado, registro_usuario
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('inicio/', redireccion_post_login, name='redireccion_post_login'),
    path('datos-personales/', datos_personales, name='datos_personales'),
    path('bloque-2/', bloque2, name='bloque2'),
    path('bloque-3/', bloque3, name='bloque3'),
    path('bloque-4/', bloque4, name='bloque4'),
    path('finalizado/', registro_finalizado, name='registro_finalizado'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', registro_usuario, name='registro_usuario'),
]
