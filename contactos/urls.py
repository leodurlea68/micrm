from django.urls import path
from . import views

urlpatterns = [
    path('crear-admin/', views.crear_admin, name='crear_admin'),
    path('migrar/', views.migrar_bd, name='migrar_bd'),
    path('', views.dashboard, name='dashboard'),
    path('contactos/', views.lista_contactos, name='lista_contactos'),
    path('contactos/<int:pk>/', views.detalle_contacto, name='detalle_contacto'),
    path('empresas/', views.lista_empresas, name='lista_empresas'),
    path('contactos/nuevo/', views.crear_contacto, name='crear_contacto'),
    path('contactos/<int:pk>/editar', views.editar_contacto, name='editar_contacto'),
    path('contactos/<int:pk>/eliminar/', views.eliminar_contacto, name= 'eliminar_contacto'),
    path('empresas/', views.lista_empresas, name='lista_empresas'),

]