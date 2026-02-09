# registro/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import (
    RegistroCeneval,
    DatosPersonales,
    Bloque2Trayectoria,
    Bloque4EntornoSocial
)

from .forms import DatosPersonalesForm, Bloque2TrayectoriaForm, Bloque3Form, Bloque4Form, RegistroUsuarioForm

@login_required
def datos_personales(request):
    registro, _ = RegistroCeneval.objects.get_or_create(usuario=request.user)

    datos = getattr(registro, 'datospersonales', None)

    if request.method == 'POST':
        form = DatosPersonalesForm(request.POST, instance=datos)
        if form.is_valid():
            datos_personales = form.save(commit=False)
            datos_personales.registro = registro
            datos_personales.save()

            registro.seccion_actual = 2
            registro.save()

            return redirect('bloque2')
    else:
        form = DatosPersonalesForm(instance=datos)

    return render(request, 'registro/datos_personales.html', {
        'form': form
    })
    
@login_required
def redireccion_post_login(request):
    registro, _ = RegistroCeneval.objects.get_or_create(usuario=request.user)

    if registro.completo:
        return redirect('registro_finalizado')

    if registro.seccion_actual == 1:
        return redirect('datos_personales')
    elif registro.seccion_actual == 2:
        return redirect('datos_academicos')
    elif registro.seccion_actual == 3:
        return redirect('contacto')
    elif registro.seccion_actual == 4:
        return redirect('antecedentes')
    else:
        return redirect('confirmacion')    

@login_required
def bloque2(request):
    bloque, creado = Bloque2Trayectoria.objects.get_or_create(
        usuario=request.user
    )

    if request.method == 'POST':
        form = Bloque2TrayectoriaForm(request.POST, instance=bloque)
        if form.is_valid():
            form.save()
            return redirect('bloque3')  # o a donde siga
    else:
        form = Bloque2TrayectoriaForm(instance=bloque)

    return render(request, 'registro/bloque2.html', {
        'form': form
    })

@login_required
def bloque3(request):
    if hasattr(request.user, 'bloque3caracteristicasescuela'):
        return redirect('bloque4')  # luego lo ajustamos

    if request.method == 'POST':
        form = Bloque3Form(request.POST)
        if form.is_valid():
            bloque = form.save(commit=False)
            bloque.usuario = request.user
            bloque.save()
            return redirect('bloque4')
    else:
        form = Bloque3Form()

    return render(request, 'registro/bloque3_caracteristicas_escuela.html', {
    'form': form
})

@login_required
def bloque4(request):
    bloque, _ = Bloque4EntornoSocial.objects.get_or_create(
        usuario=request.user
    )

    if request.method == 'POST':
        form = Bloque4Form(request.POST, instance=bloque)
        if form.is_valid():
            form.save()

            registro = RegistroCeneval.objects.get(usuario=request.user)
            registro.completo = True
            registro.save()

            return redirect('registro_finalizado')
    else:
        form = Bloque4Form(instance=bloque)

    return render(request, 'registro/bloque4_entorno_social.html', {
        'form': form
    })
    
@login_required
def registro_finalizado(request):
    registro = RegistroCeneval.objects.get(usuario=request.user)

    # Si alguien intenta entrar sin haber completado todo
    if not registro.completo:
        return redirect('redireccion_post_login')

    return render(request, 'registro/registro_finalizado.html')    

def registro_usuario(request):
    if request.user.is_authenticated:
        return redirect('redireccion_post_login')

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Crear registro base CENEVAL
            RegistroCeneval.objects.create(
                usuario=user,
                seccion_actual=1
            )

            login(request, user)
            return redirect('datos_personales')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'auth/registro_usuario.html', {
        'form': form
    })