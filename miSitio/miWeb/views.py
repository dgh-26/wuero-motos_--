from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import MensajeContacto


def inicio(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def galeria(request):
    template = loader.get_template('galeria.html')
    return HttpResponse(template.render({}, request))


def nosotros(request):
    template = loader.get_template('nosotros.html')
    return HttpResponse(template.render({}, request))


def servicios(request):
    template = loader.get_template('servicios.html')
    return HttpResponse(template.render({}, request))


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