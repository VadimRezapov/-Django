from django.core.management.base import BaseCommand
from firstapp3.models import Product


class Command(BaseCommand):
    help = 'Find product by ID and return'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        self.stdout.write(str(product))