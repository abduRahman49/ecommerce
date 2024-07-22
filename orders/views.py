from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Produit, Client
from .decorators import decorator, is_user_authenticated
from datetime import datetime


def index(request):
    context = {
        "nom": "abdou",
        "class": "django",
        "date": datetime.now(),
        "etudiants": ["Etudiant 1", "Etudiant 2", "Etudiant 3"]
    }
    return render(request, "orders/index.html", context)


def hello(request):
    produits = Produit.objects.all()
    lists = [f"<li>{p.libelle}</li>" for p in produits]
    
    html = f"""
        <h3>Produits</h3>
        <ul>
           { "".join(lists) }
        </ul>
    """
    return HttpResponse(html)


def client_infos(request, id):
    try:
        client = Client.objects.get(pk=id)
    except Client.DoesNotExist:
        raise Http404("Le client n'existe pas!")
    
    client = get_object_or_404(Client, )
    commande = client.commandes.all()[3]
    products = commande.produits.all()
    divs = [f"""
        <div> 
            <p> {p.libelle.title()} </p>
            <p> {p.prix} </p>
            <p> {p.disponibilite} </p>
            <br>
         </div>
     
     """ for p in products]

    html = f"""
        <h3>Client</h3>
        <p>Nom et Prénom: {client.first_name} {client.last_name}</p>
        <br>
        <h3>Commande</h3>
        <p>N° commande: {commande.numero_commande}</p>
        <p>Date commande: {commande.created_at}</p>
        <br>
        <h3>Produits</h3>
        {"".join(divs)}
    """
    return HttpResponse(html)


@is_user_authenticated
def process_test_request(request):
    if request.method == "POST":
        # traitement
        pass
    
    if request.method == "PUT":
        # traitement
        pass

    if request.method == "DELETE":
        # traitement
        pass
    
    return HttpResponse('You can pass')


class HomeView(View):

    @method_decorator(is_user_authenticated)
    def get(self, request):
        return HttpResponse('This is get method')

    @method_decorator(csrf_exempt)
    def post(self, request):
        print(request.POST)
        return HttpResponse('This is post method')

    @method_decorator(csrf_exempt)
    def put(self, request):
        return HttpResponse('This is put method')

    @method_decorator(csrf_exempt)
    def delete(self, request):
        return HttpResponse('This is delete method')


def list_products(request):
    products = Produit.objects.all()
    return render(request, 'orders/list_products.html', {'produits': products})
