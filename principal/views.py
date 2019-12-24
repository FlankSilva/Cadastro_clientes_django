from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def article(request, year):
    return HttpResponse(f'O ano informado foi: {str(year)}')

