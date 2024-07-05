from django.core.management.base import BaseCommand
from firstapp3.models import Client


class Command(BaseCommand):
    help = 'Create client by params: name mail phone address'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('mail', type=str, help='Client mail format: client@example.com')
        parser.add_argument('phone', type=str, help='Client phone number format: +79998887766')
        parser.add_argument('address', type=str, help='Client phone address format: City, Street, Home number')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        mail = kwargs.get('mail')
        phone = kwargs.get('phone')
        address = kwargs.get('address')
        client = Client(name=name, mail=mail, phone=phone, address=address)
        client.save()