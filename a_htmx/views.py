from django.shortcuts import render
from django.http import HttpResponse
import requests

def htmx_view(request): 
    return render(request, 'index.html')

counter = 1
def users_detail(request): 
    global counter 
    # users =[
    #     'Prashant Kumar Gupta',
    #     'Nishant Kumar Gupta', 
    #     'Amrita Tiwari', 
    #     'Ravi Gupta', 
    #     'Pramod Ganjhu',
    # ]
    counter += 1; 

    response = requests.get('https://jsonplaceholder.typicode.com/users')
    data = response.json() 

    return render(request, 'snippets/users.html', {'users': data, 'counter': counter})

