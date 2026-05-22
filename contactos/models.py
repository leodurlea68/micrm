from django.db import models
from django.urls import reverse

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Empresas"

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    cargo = models.CharField(max_length=100, blank=True)
    
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    notas = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}".strip()
    
    def get_full_name(self):
        return f"{self.nombre} {self.apellido}".strip()

class Interaccion(models.Model):
    TIPO_CHOICES = [
        ('llamada', 'Llamada'),
        ('email', 'Email'),
        ('reunion', 'Reunión'),
        ('whatsapp', 'WhatsApp'),
        ('otro', 'Otro'),
    ]
    
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE, related_name='interacciones')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    proximo_seguimiento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.tipo} con {self.contacto} - {self.fecha.date()}"