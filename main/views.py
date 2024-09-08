from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Laughing Gas',
        'price': '$ 20',
        'description': 'Laughing on the go'
    }

    return render(request, "main.html", context)