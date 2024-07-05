import decimal

from django.core.management.base import BaseCommand
from firstapp3.models import Client, Product, Order
from . import get_client, get_product


class Command(BaseCommand):
    help = 'Create order by params: customerID productID price'

    def add_arguments(self, parser):
        parser.add_argument('client_pk', type=int, help='Client ID')
        parser.add_argument('products_pk', type=str, help='Products ID ')
        parser.add_argument('total_price', type=float, help='Order price')

    def handle(self, *args, **kwargs):
        client_pk = kwargs.get('client_pk')
        customer = Client.objects.filter(pk=client_pk).first()
        price = kwargs.get('total_price')
        order = Order(customer=customer, total_price=price)
        order.save()
        products_pk = kwargs.get('products_pk').split('-')
        products = [Product.objects.filter(pk=prod_pk).first() for prod_pk in products_pk]
        order.products.add(*[int(pk) for pk in products_pk])