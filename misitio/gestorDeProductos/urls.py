from django.urls import path
from . import views
# mis urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('registro', views.registro, name='registro'),
    path('galeria', views.galeria, name='galeria'),
    path('sucursal', views.sucursal, name='sucursal'),
    path('producto', views.producto, name='producto'),
    path('logout', views.logout),

]