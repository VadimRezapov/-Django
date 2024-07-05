from django.core.management.base import BaseCommand
from firstapp2.models import Client


class Command(BaseCommand):
    help = 'Update client name'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')
        # parser.add_argument('mail', type=str, help='Client mail format: client@example.com')
        # parser.add_argument('phone', type=str, help='Client phone number format: +79998887766')
        # parser.add_argument('address', type=str, help='Client phone address format: City, Street, Home number')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        # mail = kwargs.get('mail')
        # phone = kwargs.get('phone')
        # address = kwargs.get('address')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.name = name
            client.save()