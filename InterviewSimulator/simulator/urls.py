from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_question, name='add_question'),
    path('questions/', views.question_list, name='questions'),
    path('start/', views.start_interview, name='start_interview'),
]
