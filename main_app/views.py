from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Dog

from main_app.models import Dog
# Create your views here.

class DogList(ListView):
    model = Dog

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/' 

class DogDelete(DeleteView):
    model = Dog
    success_url = '/' 
