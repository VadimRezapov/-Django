from django.core.management.base import BaseCommand
from firstapp3.models import Product


class Command(BaseCommand):
    help = 'Create product by params: '

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Product title')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=str, help='Product price')
        parser.add_argument('quantity', type=int, help='Product quantity')

    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        desc = kwargs.get('description')
        price = kwargs.get('price')
        qnt = kwargs.get('quantity')
        product = Product(title=title, description=desc, price=price, quantity=qnt)
        product.save()