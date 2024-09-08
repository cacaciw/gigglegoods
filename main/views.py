from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'App' : 'Giggle Goods',
        'Name': 'Tarissa Mutia Andini',
        'Class': 'PBP C'
    }

    return render(request, "main.html", context)