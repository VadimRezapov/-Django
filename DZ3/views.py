from datetime import timedelta, date

from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Product, Order


def index(request):
    return HttpResponse('Main page HW_3')


def client_orders(request, client_id: int):
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(customer=client).all()
    print(f'{orders=}')
    orders_base = {}
    for order in orders:
        products = order.products.all()
        products = set([product.__str__() for product in products])
        orders_base.setdefault(str(order.pk), products)
    print(f'{orders_base=}')
    context = {'client': client.name, 'orders_base': orders_base}
    # return HttpResponse('client_orders')
    return render(request, 'firstapp3/index.html', context)


def client_orders_period(request, client_id: int, period_days: int):
    client = Client.objects.filter(pk=client_id).first()
    timespan = timedelta(days=period_days)
    orders = Order.objects.filter(customer=client).filter(date_order__gt=(date.today() - timespan))
    print(f'{orders=}')
    orders_base = {}
    for order in orders:
        products = order.products.all()
        products = set([product.__str__() for product in products])
        orders_base.setdefault(order, products)
    print(f'{orders_base=}')
    context = {'client': client.name, 'orders_base': orders_base, 'period': period_days}
    # return HttpResponse('client_orders')
    return render(request, 'firstapp3/orders.html', context)