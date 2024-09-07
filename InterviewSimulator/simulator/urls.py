# simulator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('interview/', views.interview, name='interview'),
    path('setup/', views.setup, name='interview_setup'),
    path('setup_interview/', views.setup_interview, name='setup_interview'),
    path('interview_home/', views.interview, name='interview_home'),
    path('ideal_answers/', views.ideal_answers_view, name='ideal_answers'),
    path('answer_questions/', views.answer_questions, name='answer_questions'),
]
