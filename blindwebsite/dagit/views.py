from django.shortcuts import render
from dagit.models import Gonderi

def dagit_index(request):
    gonderiler = Gonderi.objects.all()
    context = {
        "gonderiler": gonderiler,
    }
    return render(request, "dagit_index.html", context)

def dagit_kategori(request, kategori):
    gonderiler = Gonderi.objects.filter(
        kategoriler__name__contains=kategori
    )
    
    context = {
        "kategori": kategori,
        "gonderiler": gonderiler
    }
    return render(request, "dagit_kategori.html", context)

def dagit_detail(request, pk):
    gonderi = Gonderi.objects.get(pk=pk)
    
    context = {"gonderi": gonderi}
    return render(request, "dagit_detail.html", context)