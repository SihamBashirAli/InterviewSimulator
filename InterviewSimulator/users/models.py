from django.db import models
from .train import train_model 

# Create your models here.
class InterviewQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()
    
def train_model():
    # Placeholder for training function
    print("Training model...")

def train_view(request):
    train_model()
    return render(request, 'ai/train.html')

