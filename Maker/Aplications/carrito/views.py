from django.shortcuts import render
from django.http import JsonResponse
import json
from Aplications.Usuarios.models import User
from Aplications.pedido.models import Pedido



def int(request):
    return render(request,'Carrito/carrito.html')
# Create your views here.



def carrito(request):
    if request.user.is_authenticated:
        customer = request.user
        pedido, created = Pedido.objects.get_or_create(Usuario_p=customer)
        items = pedido.carritoproducto_set.all()
        # pedido es la foreign key de carritoproducto
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'pedido': pedido}
    return render(request, 'Carrito/carrito.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Producto ID:', productId)
    return JsonResponse('IS FUNCIONAL',safe=False)