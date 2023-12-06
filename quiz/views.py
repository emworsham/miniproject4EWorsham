from django.shortcuts import render
from .models import Question, QuizAttempt
from django.contrib.auth.decorators import login_required
import random

def register(request):
    # Handle user registration
    pass

def login(request):
    # Handle user login
    pass

@login_required
def take_quiz(request):
    # Randomly select 5 questions
    questions = list(Question.objects.all())
    random_questions = random.sample(questions, 5)

    # Render these questions in a template
    pass

@login_required
def quiz_results(request):
    # Display user's quiz attempts and scores
    pass

def admin_page(request):
    # Custom admin view for managing questions/choices
    pass

