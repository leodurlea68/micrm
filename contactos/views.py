from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Contacto, Empresa, Interaccion
from django.db.models import Count
from django.db import models
from .forms import ContactoForm 

#@login_required
def dashboard(request):
    total_contactos = Contacto.objects.count()
    total_empresas = Empresa.objects.count()
    ultimos_contactos = Contacto.objects.order_by('-fecha_creacion')[:5]
    
    context = {
        'total_contactos': total_contactos,
        'total_empresas': total_empresas,
        'ultimos_contactos': ultimos_contactos,
    }
    return render(request, 'contactos/dashboard.html', context)

#@login_required
def lista_contactos(request):
    contactos = Contacto.objects.all().select_related('empresa')
    return render(request, 'contactos/lista_contactos.html', {'contactos': contactos})
def lista_contactos(request):
    query = request.GET.get('q', '')
    if query:
        contactos = Contacto.objects.filter(
            models.Q(nombre__icontains=query) |
            models.Q(apellido__icontains=query) |
            models.Q(email__icontains=query) |
            models.Q(empresa__nombre__icontains=query)
        ).select_related('empresa')
    else:
        contactos = Contacto.objects.all().select_related('empresa')
    
    return render(request, 'contactos/lista_contactos.html', {
        'contactos': contactos,
        'query': query
    })

#@login_required
def detalle_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'contactos/detalle_contacto.html', {'contacto': contacto})

#@login_required
def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'contactos/lista_empresas.html', {'empresas': empresas})

#@login_required
def crear_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
    return render(request, 'contactos/crear_contacto.html', {'form': form})

#@login_required
def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('detalle_contacto', pk=contacto.pk)
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'contactos/editar_contacto.html', {'form': form, 'contacto': contacto})

#@login_required
def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'contactos/eliminar_contacto.html', {'contacto': contacto})