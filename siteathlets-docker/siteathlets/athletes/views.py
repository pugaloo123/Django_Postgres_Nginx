from django.views.generic import ListView, DetailView
from .models import Athlete


class AthleteListView(ListView):
    model = Athlete
    template_name = 'athletes/list.html'
    context_object_name = 'athletes'


class AthleteDetailView(DetailView):
    model = Athlete
    template_name = 'athletes/detail.html'
    context_object_name = 'athlete'
