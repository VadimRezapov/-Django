from django.shortcuts import render


def index(request):
    return render(request, 'firstapp6/index.html')