from django.shortcuts import render, redirect
from main.forms import GiggleForm
from main.models import GiggleCatalogue


# Create your views here.
def show_main(request):
    giggle_entry = GiggleCatalogue.objects.all()
    context = {
        'App' : 'Giggle Goods',
        'Name': 'Tarissa Mutia Andini',
        'Class': 'PBP C',
        'giggle_entries': giggle_entry,
    }

    return render(request, "main.html", context)

def create_giggle_entry(request):
    form = GiggleForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_giggle_entry.html", context)