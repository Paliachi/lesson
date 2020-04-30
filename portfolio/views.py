from django.shortcuts import render , get_object_or_404
from .models import Project

def home (request):
    projects = Project.objects.all()
    return render (request, 'home.html', {"projects":projects})

def sac (request, portfolio_id):
    idi = get_object_or_404(Project, pk=portfolio_id)
    return render (request, 'sac.html', {"idi":idi})
