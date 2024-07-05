from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Main Page HW_2. На этом уроке создавали модели, поэтому смотреть нечего.')