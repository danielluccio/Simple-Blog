from django.urls import path
from App.views import post_list


urlpatterns = [
    path('', post_list, name='post_list'),
    
]