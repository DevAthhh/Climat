from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import requests
from django.views.decorators.http import require_http_methods

from main.utils.get_weather import get_weather


def index(request):
    if request.method == 'POST':
        request.session['city'] = request.POST.get('city')
        return redirect('home')
    try:
        city = request.session.get('city')
        if city:
            temp = get_weather(city)
        else:
            city = 'None'
            temp = 'None'
    except:
        city = 'Москва'
        temp = 'None'
    return render(request, 'main/index.html', context={'title': 'Погода',
                                                       'city': city,
                                                       'temperature': temp[1],
                                                       'feels_like': temp[2],
                                                       'weather': temp[0]})