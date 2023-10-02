from django.shortcuts import render,redirect
from .models import User
from Aplications.productos.models import Producto
from .forms import Userform,Authformi
from django.contrib.auth import login, logout,authenticate
from django.db import IntegrityError
from django.contrib import messages

from django.template import loader
# Create your views here.
def prueba(request):
    tabla = Userform
    
    return render (request,'Main.html',{'form': tabla})

def home(request):
    products = Producto.objects.all()
    return render(request,'Main.html',{'product':products})

def User_regist(request):
    tabla = Userform()
    
    if request.method == 'GET':
        print('Obteiendo datos')
        return render(request,'Registros/register.html',{'form':tabla})
    else:
        #Comprobacion de si los textbox tienen el mismo password
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                user = User.objects.create_user(email=request.POST['email'],nombre=request.POST['nombre'] ,apellido=request.POST['apellido'],password=request.POST['password1'])
                print(request.POST)
                user.save()
                login(request,user)
                return redirect('padre')
            except IntegrityError:
                print('Recibiendo datos')
                error = 'Usuario ya registrado intente con otro'
                return render(request,'Registros/register.html',{'form':tabla,'error':error})
            
        return render(request,'Registros/register.html',{'form':tabla,'error':'No coinciden passwords'})



def init(request):
    if request.method == 'GET':
        aut = Authformi
        print('terrible ayuda')
        return render(request,'Registros/register.html',{'form':aut})
    else:
         user = authenticate(request,email=request.POST['email'],password=request.POST['password'])
       
         if user is None:
             aut = Authformi
             return render(request,'Registros/register.html',{'form':aut,'error': 'NO gay no exite'})
         else:
           login(request,user)
           messages.success(request,"iniaciado correct")
           return redirect('padre')
        
        
        


def log_out(request):
    logout(request)
    
    return redirect('padre')
