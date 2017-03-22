from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.views.generic.list import ListView

from productes.models import Producte, Carrito, Detall

from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm

class ProducteListView(ListView):
	model = Producte
	model2 = Detall

class MostraCarritoView(ListView):
	model = Carrito

def afegeix(request, producte_id):
	carro = Carrito.objects.filter(obert=True).count()
	contCarros = Carrito.objects.count()
	num = contCarros + 1
	if( carro ):
		# si hi ha carro obert, l'omplo
		carro = Carrito.objects.filter(obert=True)[0]
	else:
		# si no, el creo
		carro = Carrito()
		carro.nom = "Prova "+ str(num)
		carro.save()

	detall = Detall()
	detall.carrito = carro
	detall.producte = Producte.objects.get(pk=producte_id)
	detall.quantitat = 1
	detall.save()

	return redirect("/")

def tancar(request):
	carro = Carrito.objects.filter(obert=True)[0]
	carro.obert = False
	carro.save()
	return redirect('/')

def producte(request, id):
    template = loader.get_template('productes/product.html')
    context = {
        'product': Producte.objects.get(id=id)
    }
    return HttpResponse(template.render(context, request))

def carrito(request, id):
    template = loader.get_template('productes/carrito.html')
    carro = Carrito.objects.get(id=id)
    context = {
        'detalls': Detall.objects.filter(carrito=carro)
    }
    return HttpResponse(template.render(context, request))

def abrir(request, id):
	abiertos = Carrito.objects.filter(obert=True).count()

	if (abiertos>0):
		carro2 = Carrito.objects.filter(obert=True)[0]
		carro2.obert = False
		carro2.save()
	
	carro = Carrito.objects.filter(id=id)[0]
	carro.obert = True
	carro.save()
	
	return redirect('/')