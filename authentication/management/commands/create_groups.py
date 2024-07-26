from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "Permet de créer un groupe d'utilisateurs"

    def add_arguments(self, parser):
        # Permet de récupérer les arguments de la commande et les stocker dans une liste qui aura pour nom le premier argument de parser.add_argument()
        parser.add_argument("group_names", nargs="+", type=str)

    def handle(self, *args, **options):
        # Permet d'effectuer les opérations que l'on souhaite automatiser et définir comme commande d'administration
        group_names = options["group_names"]
        for group_name in group_names:
            # Récupère ou crée le groupe (groupe de permissions auquel des utilisateurs peuvent être ajoutés)
            _, created = Group.objects.get_or_create(
                name=group_name
            )
            if not created:  # Si le groupe n'est pas créé alors il existe déja et la variable created sera évaluée à False
                raise CommandError(f'Le groupe avec le nom {group_name} existe déjà')

            self.stdout.write(
                self.style.SUCCESS(f'Le groupe {group_name} a été créé avec succès')
            )
