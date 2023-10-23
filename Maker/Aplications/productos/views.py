from django.shortcuts import render,redirect,get_object_or_404
from Aplications.productos.models import Producto
from Aplications.Usuarios.views import home
from .forms import Producto_f

def cart(request,id):
    
    productos = Producto.objects.filter(id=id)
    
    print(productos)
    
    
    return render(request,'productos/detail_p.html',{'productos':productos})


def carga_p(request):
    try:
        if request.method == 'GET':
            prod = Producto_f()
            return render(request,'productos/carga_p.html',{'form':prod})
        else:
            prod = Producto_f(data=request.POST,files=request.FILES)
            if prod.is_valid():
                print('pasa')
                prod.save()
                return redirect(to='padre')
                
            else:
               print('No funciona')
               return render(request,'productos/carga_p.html',{'form':prod})
                 
    except ValueError as i:
        print(i)



def modify_p(request,id):
    products = get_object_or_404(Producto,id=id)
    try:
        if request.method == 'GET':
            data ={
                'form': Producto_f(instance=products) 
            }
            return render (request,'productos/modificar.html',data)
        else:
            products = get_object_or_404(Producto,id=id)
            formulario = Producto_f(data=request.POST,instance=products,files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                print('valid')
                return redirect(to='padre')
    except ValueError as e:
        print(e)
            
        
# Create your views here.
