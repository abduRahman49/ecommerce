from django.db import models
from uuid import uuid4


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)


class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    numero_commande = models.UUIDField(default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="commandes")


class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=100)
    description = models.TextField(null=True)
    prix = models.FloatField()
    disponible = models.BooleanField()
    image = models.ImageField(upload_to="images/")
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name="produits", null=True)


    @property
    def disponibilite(self):
        if not self.disponible:
            return "Non disponible"
        
        return "Disponible"

class Categorie(models.Model):
    libelle = models.CharField(max_length=100)
    produits = models.ManyToManyField(Produit, null=True)
