from django.urls import path
from taskApp import views

urlpatterns = [
    path('', views.index),
    path('completed/<task_id>', views.completed,name = 'completed'),
    path('pending/<task_id>', views.pending,name = 'pending')
]
