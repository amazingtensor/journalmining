"""Defines application "logic". Connects models and templates.
Decide what model will be displayed and pass to template
"""
from django.shortcuts import render
from .models import Listing # where . means current directory or current application


def predatoryjournals_list(request):
    journals = Listing.objects.filter(journaltitle__contains='Journal')
    return render(request, 'predatoryjournals/predatoryjournals.html', {'journals': journals})
