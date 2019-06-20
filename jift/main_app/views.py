from .models import *
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError


def index(request):
    context = {}
    return render(request, 'index.html', context)


def predict(request):
    context = {}
    if request.method == 'POST':
        f = PredictForm(request.POST)
        if f.is_valid():
            p_list = Product.objects.all()
            context['p_list'] = p_list

    else:
        f = PredictForm()

    context['form'] = f
    return render(request, 'predict.html', context)


def item(request, item_id):
    context = {}
    item_obj = Product.objects.filter(id=int(item_id)).get()
    context['name'] = str(item_obj.name)
    context['description'] = str(item_obj.description)
    context['link'] = str(item_obj.link)
    context['item_id'] = int(item_obj.id)
    print(context['item_id'])
    return render(request, 'item.html', context)

