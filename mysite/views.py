from django.shortcuts import render
from .models import Devices
# Create your views here.
def home_page(request):
    return render(request, 'home_page.html', {'devices': Devices.objects.all()})