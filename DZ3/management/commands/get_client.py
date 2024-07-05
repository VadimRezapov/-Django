from django.core.management.base import BaseCommand

from firstapp3.models import Client


class Command(BaseCommand):
    help = 'Find client by ID and return'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(str(client))