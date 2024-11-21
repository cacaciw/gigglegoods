from django.shortcuts import render, redirect, reverse
from main.forms import GiggleForm
from main.models import GiggleCatalogue
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout



def landing_page(request):
    return render(request, 'landing.html')

def home_page(request):
    return render(request, 'home.html')


@login_required(login_url='/login')
def show_main(request):
    #giggle_entries = GiggleCatalogue.objects.filter(user=request.user)
    context = {
        'App' : 'Giggle Goods',
        'Name': request.user.username,
        'Class': 'PBP C',
        #'giggle_entries': giggle_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_giggle_entry(request):
    form = GiggleForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        giggle_entry = form.save(commit=False)
        giggle_entry.user= request.user
        giggle_entry.save()
        return redirect('main:show_main')


    context = {'form': form}
    return render(request, "create_giggle_entry.html", context)

def show_xml(request):
    data = GiggleCatalogue.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = GiggleCatalogue.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = GiggleCatalogue.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = GiggleCatalogue.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = GiggleCatalogue.objects.get(pk = id)

    form = GiggleForm(request.POST or None, instance= product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Ambil product dari id nya
    product = GiggleCatalogue.objects.get(pk = id)
    product.delete() #Hapus productnya
    return HttpResponseRedirect(reverse('main:show_main')) # Kembali ke halaman awal


@csrf_exempt  # Only keep this if absolutely necessary
@require_POST
def add_giggle_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    giggleLevel = strip_tags(request.POST.get("giggleLevel"))

    if name and price and description:
        giggle_entry = GiggleCatalogue.objects.create(
            user=request.user,
            name=name,
            price=price,
            description=description,
            giggleLevel= giggleLevel
        )
        return JsonResponse({'success': True, 'id': giggle_entry.pk})
    else:
        return JsonResponse({'success': False})
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_product = GiggleCatalogue.objects.create(
                name=data["Name"],
                description=data["Description"],
                price=int(data["Price"]),
                giggleLevel=int(data["GiggleLevel"]),
                user=request.user 
            )
            new_product.save()
            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=401)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)