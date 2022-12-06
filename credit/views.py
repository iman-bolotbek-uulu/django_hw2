from django.shortcuts import render, get_object_or_404,reverse
from django.http import HttpResponse,HttpResponseRedirect
from . import models
from django.views import generic


# Create your views here.
class ClientListView(generic.ListView):
    model = models.Client
    template_name = 'index.html'


class ClientDetailView(generic.DetailView):
    model = models.Client