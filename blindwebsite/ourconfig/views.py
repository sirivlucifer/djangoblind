from django.shortcuts import render
from ourconfig.models import Config

# Create your views here.

def ourconfig_index(request):
    ourconfigs=Config.objects.all()
    context = {
        "ourconfigs" : ourconfigs,
    }
    return render(request, "ourconfig_index.html",context)

