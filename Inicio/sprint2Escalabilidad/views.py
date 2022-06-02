import hashlib
from sre_constants import SUCCESS
from django.shortcuts import render
from . import models
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
from django.core.mail import send_mail  
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
import random




ipValidas = ['127.0.0.1']

def index(request):
    return render(request, 'formulario.html')

def inicio(request):#Primra vista
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        
    if (ip not in ipValidas):
            
            print("llego")
            '''
            htmly = get_template('Email.html')
            #d = { 'username': "Diego" }
            subject, from_email, to = 'Una ip desconocida esta intentando acceder a tu información', 'educacionestrellafake@gmail.com', "thalassamania@gmail.com"
            html_content = htmly.render()
            
            #msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            #msg.attach_alternative(html_content, "text/html")
            #msg.send()'''
            return render(request, 'formulario.html')

    return render(request, 'index.html')

class rejected (SuccessMessageMixin) :
    templete_name = 'index.html'
    email_templeate_name = 'Emeail.html'
    success_url = reverse_lazy('index.html')
     

def hashing2(archivo):
    with open(archivo, 'rb') as f: 
        md5 = hashlib.md5() 

    for chunk in iter(lambda: f.read(4096), b""): 
        md5.update(chunk)  
    return (md5.hexdigest()) 


def createHash():
    """This function generate 10 character long hash"""
    return hexlify(os.urandom(5))
    
def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile,
            )


        
        if (document.DoesNotExist):
            document.save()
        else:
            htmly = get_template('Email.html')
            d = { 'username': "Nombre de Prueba" }
            subject, from_email, to = 'Se ha intentado Cambiar un Archivo', 'educacionestrellafake@gmail.com', "d.rodriguez57@uniandes.edu.co"
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        
    documents = models.Document.objects.all()

    return render(request, "formulario.html", context = {
        "files": documents
    })



  