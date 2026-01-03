from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def property_detail(request, property_id):
    # Minimal view implementation to avoid import errors during startup.
    # Replace with real model lookup and template rendering later.
    return HttpResponse(f"Property detail page for id: {property_id}")