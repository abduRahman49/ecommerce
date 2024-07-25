from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "Permet de créer un groupe d'utilisateurs"

    def add_arguments(self, parser):
        parser.add_argument("group_names", nargs="+", type=str)

    def handle(self, *args, **options):
        group_names = options["group_names"]
        for group_name in group_names:
            _, created = Group.objects.get_or_create(
                name=group_name
            )
            if not created:
                raise CommandError(f'Le groupe avec le nom {group_name} existe déjà')

            self.stdout.write(
                self.style.SUCCESS(f'Le groupe {group_name} a été créé avec succès')
            )
