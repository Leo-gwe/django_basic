from django.http import HttpResponse
from django.shortcuts import render
from properties.models import Property

# Create your views here, home function below
def home(request):
    properties = Property.objects.all()
    context = {
        'properties': properties,
    }
    return render(request, 'home.html', context)