from django.urls import path
from App.views import post_list, post_details, create_post, post_update, post_delete


urlpatterns = [
    path('', post_list, name='post_list'),
    path('post_details/<int:id>/' , post_details, name='post_details'),
    path('post_create', create_post, name='post_create'),
    path('post_update/<int:id>/', post_update, name='post_update'),
    path('post_delete<int:id>/',  post_delete, name='post_delete')
]