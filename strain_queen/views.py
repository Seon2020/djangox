from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Strain
from django.urls import reverse_lazy

class StrainListView(ListView):
    template_name = 'strain_list.html'
    model = Strain

class StrainDetailView(DetailView):
    template_name = 'strain_detail.html'
    model = Strain

class StrainCreateView(CreateView):
    template_name = 'strain_create.html'
    model = Strain
    fields = ['name', 'strain_type', 'description', 'smoker']
    success_url = reverse_lazy('strain_list')

class StrainUpdateView(UpdateView):
    template_name = 'strain_update.html'
    model = Strain
    fields = ['name', 'strain_type', 'description', 'smoker']
    success_url = reverse_lazy('strain_list')

class StrainDeleteView(DeleteView):
    template_name = 'strain_delete.html'
    model = Strain
    success_url = reverse_lazy('strain_list')