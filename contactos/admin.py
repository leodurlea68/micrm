from django.contrib import admin
from .models import Empresa, Contacto, Interaccion

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha_creacion')
    search_fields = ('nombre', 'email')

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'empresa', 'fecha_creacion')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('empresa',)

@admin.register(Interaccion)
class InteraccionAdmin(admin.ModelAdmin):
    list_display = ('contacto', 'tipo', 'fecha', 'proximo_seguimiento')
    list_filter = ('tipo',)
    search_fields = ('contacto__nombre', 'descripcion')