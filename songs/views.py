from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Song

# Create your views here.
class SongListView(ListView):
    model = Song
    template_name = 'song-list.html'

class SongDetailView(DetailView):
    model = Song
    template_name = 'song-detail.html'

class SongCreateView(CreateView):
    model = Song
    template_name ='song-create.html'
    fields = ["name", "genre", "purchaser"]

class SongUpdateView(UpdateView):
    model = Song
    template_name ='song-update.html'
    fields = ["name", "genre", "purchaser"]

class SongDeleteView(DeleteView):
    model = Song
    template_name ='song-delete.html'
    success_url = reverse_lazy('song-list')
    success_url = '/'

