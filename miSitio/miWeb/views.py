from django.shortcuts import render
from .models import MensajeContacto


def inicio(request):
    return render(request, 'index.html')


def galeria(request):
    return render(request, 'galeria.html')


def nosotros(request):
    return render(request, 'nosotros.html')


def servicios(request):
    return render(request, 'servicios.html')


def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        servicio = request.POST.get('servicio', '').strip()
        mensaje = request.POST.get('mensaje', '').strip()

        if nombre and telefono and servicio and mensaje:
            MensajeContacto.objects.create(
                nombre=nombre,
                telefono=telefono,
                servicio=servicio,
                mensaje=mensaje
            )

            return render(request, 'contacto.html', {
                'exito': '¡Tu mensaje se guardó correctamente!',
                'datos_whatsapp': {
                    'nombre': nombre,
                    'telefono': telefono,
                    'servicio': servicio,
                    'mensaje': mensaje
                }
            })

        return render(request, 'contacto.html', {
            'error': 'Completa todos los campos.'
        })

    return render(request, 'contacto.html')
    
