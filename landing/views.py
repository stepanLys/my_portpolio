from django.shortcuts import render
from .forms import *


def landing(request):
    vk = 'https://vk.com/id309124641'
    facebook = 'https://www.facebook.com/profile.php?id=100012239236894'
    git = 'https://github.com/stepanLys'

    form = OrderForm(request.POST or None)

    return render(request, 'landing/landing.html', locals())