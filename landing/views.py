from django.shortcuts import render
from .forms import *
from my_works.models import *


def landing(request):
    vk = 'https://vk.com/id309124641'
    facebook = 'https://www.facebook.com/profile.php?id=100012239236894'
    git = 'https://github.com/stepanLys'
    my_email = 'stepan.lys98@gmail.com'
    my_phone = '+380-93-86-40-768'


    form = OrderForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    works = Work.objects.filter(is_active=True)

    return render(request, 'landing/landing.html', locals())


def test(request):
    vk = 'https://vk.com/id309124641'
    facebook = 'https://www.facebook.com/profile.php?id=100012239236894'
    git = 'https://github.com/stepanLys'

    form = OrderForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'landing/index.html', locals())