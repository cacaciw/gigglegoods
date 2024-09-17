from django.shortcuts import render, redirect
from main.forms import GiggleForm
from main.models import GiggleCatalogue
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def show_main(request):
    giggle_entries = GiggleCatalogue.objects.all()
    context = {
        'App' : 'Giggle Goods',
        'Name': 'Tarissa Mutia Andini',
        'Class': 'PBP C',
        'giggle_entries': giggle_entries,
    }

    return render(request, "main.html", context)

def create_giggle_entry(request):
    form = GiggleForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_giggle_entry.html", context)

def show_xml(request):
    data = GiggleCatalogue.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = GiggleCatalogue.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = GiggleCatalogue.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = GiggleCatalogue.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



