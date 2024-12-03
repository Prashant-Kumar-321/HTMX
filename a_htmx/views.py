from django.shortcuts import render
from django.http import HttpResponse

def htmx_view(request): 
    return render(request, 'index.html')

def users_detail(request): 
    return HttpResponse('<div class="text-lg text-orange-700">This is response from server</div>')
