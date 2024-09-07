# simulator/forms.py
from django import forms

class InterviewSetupForm(forms.Form):
    subject_area = forms.ChoiceField(choices=[('tech', 'Tech'), ('finance', 'Finance'), ('healthcare', 'Healthcare')])
    number_of_questions = forms.IntegerField(min_value=1, max_value=20)
    level_of_difficulty = forms.ChoiceField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    time_per_question = forms.IntegerField(min_value=10, max_value=300)
    industry = forms.CharField(max_length=100)
    job_role = forms.CharField(max_length=100)
    competencies = forms.CharField(max_length=200)
    interview_format = forms.ChoiceField(choices=[('behavioral', 'Behavioral'), ('technical', 'Technical'), ('case', 'Case Study'), ('panel', 'Panel')])
    question_types = forms.ChoiceField(choices=[('open-ended', 'Open-ended'), ('situational', 'Situational'), ('technical', 'Technical'), ('analytical', 'Analytical')])
    experience_level = forms.ChoiceField(choices=[('entry', 'Entry Level'), ('mid', 'Mid Level'), ('senior', 'Senior Level')])
