from django.core.management.base import BaseCommand
from firstapp2.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Create order by params: customer product price'

    def add_arguments(self, parser):
        parser.add_argument('client_pk', type=int, help='Client ID')
        parser.add_argument('product_pk', type=int, help='Product ID')
        parser.add_argument('price', type=float, help='Order price')

    def handle(self, *args, **kwargs):
        client_pk = kwargs.get('client_pk')
        customer = Client.objects.filter(pk=client_pk).first()
        product_pk = kwargs.get('product_pk')
        product = Product.objects.filter(pk=product_pk).first()
        price = kwargs.get('price')
        order = Order(customer=customer, total_price=price)
        order.save()
        order.products.add(product)