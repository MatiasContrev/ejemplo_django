from django import http
from django.http import HttpResponse
from datetime import date, datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("-----------Segunda vista------")

def dia(request):
    variable = datetime.now()
    return HttpResponse(f"Hoy es un gran día {variable}")

def apellido(request, ape):
    fecha = datetime.now()
    return HttpResponse(f"El profe de coder: {ape} es muy bueno..<br><br> Por lo menos hoy {fecha}")

def probando_template(request):
    mi_html = open("C:/Users/mafiu/Desktop/Curso Python/visual/Proyecto1/Proyecto1/plantillas/template1.html")

    plantilla = Template(mi_html.read())

    mi_html.close()

    mi_contexto =  Context()

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)
