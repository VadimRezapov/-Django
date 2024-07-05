"""
URL configuration for hwproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index, client_orders, client_orders_period

urlpatterns = [
    path("", index, name='index'),
    path("clientorders/<int:client_id>/", client_orders, name="client_orders"),
    path("periodorders/<int:client_id>/<int:period_days>/", client_orders_period, name="client_orders_period"),
]