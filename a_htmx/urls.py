from django.urls import path 

from .views import * 

urlpatterns = [
    path('', htmx_view, name='htmx'),
    path('users/', users_detail, name='users-info')
]
