from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

def cmsusersput(request, rec):
    #Código de las transparencias para la autenticación de usuario
    if request.user.is_authenticated():
        logged = "Logged in as " + request.user.username + '<br><a href="/admin/logout/">Logout</a><br><a href="/admin/">Añadir o modificar páginas</a><br>'
    else:
        logged = "Not logged in.<br><a href='/admin/login/'>Login</a><br>"
        
    #Vamos a ver los métodos que nos llegan
    
    if request.method == "GET": #Devolver los elementos
        try:
            lista = Pages.objects.get(name=rec)
            return HttpResponse(logged + lista.page)
            
        except Pages.DoesNotExist:  #Este mensaje me sale también cuando no meto nada
            return HttpResponse(logged + "La página no ha sido encontrada en la base de datos")
            
    elif request.method == "PUT":   #Añadir contenido
        if request.user.is_authenticated():
            try:
                bodyput = request.body
                lista = Pages.objects.create(name=rec, page=bodyput)
                lista.save()
                return HttpResponse("Nueva lista creada") 
            except:
                return HttpResponse("Se ha producido un error")
                
        else:
            return HttpResponse("Debe autentificarse para continuar")            
