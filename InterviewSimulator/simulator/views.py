import spacy
import random
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm

nlp = spacy.load("en_core_web_sm")
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questions')
    else:
        form = QuestionForm()
    return render(request, 'simulator/add_question.html', {'form': form})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'simulator/question_list.html', {'questions': questions})

def start_interview(request):
    questions = list(Question.objects.all())
    random.shuffle(questions)
    return render(request, 'simulator/start_interview.html', {'questions': questions})
def evaluate_response(user_response, question):
    doc = nlp(user_response)
    return len(doc.ents)  # Example: count the named entities in the response

def process_response(request):
    if request.method == 'POST':
        user_response = request.POST['response']
        question_id = request.POST['question_id']
        question
