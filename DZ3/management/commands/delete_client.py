from django.core.management.base import BaseCommand
from firstapp3.models import Client


class Command(BaseCommand):
    help = 'Update client name'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            # self.stdout.write(str(client))
            client.delete()
        self.stdout.write(str(client))