from django.shortcuts import render
from django.views.generic import ListView

from main_app.models import Item
# Create your views here.

class ItemList(ListView):
    model = Item

