from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     text = "text"
#     context = {"text" : text}
#     return render(request, 'top/index.html', context)

from django.http import HttpResponse


def index(request):
    return render(request, 'top/index.html')