from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Produit, Client


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
