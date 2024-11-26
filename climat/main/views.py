from django.shortcuts import render, redirect
from django.views.generic.base import View

from .utils.utils import get_objects_for_context


class Index(View):
    """
    This is a view class, about main page...
    """

    def get(self, request, *args, **kwargs):
        data = get_objects_for_context(request=request)
        if type(data) == dict:
            return render(request, 'main/index.html', context={'title': 'Погода',
                                                           'city': data['city'],
                                                           'temperature': data['temperature'],
                                                           'feels_like': data['feels_like'],
                                                           'weather': data['weather'],
                                                        })
        return render(request, 'main/index.html', context={'title': 'Погода',
                                                           'city': 'None',
                                                        })

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            request.session['city'] = request.POST.get('city')
            return redirect('home')