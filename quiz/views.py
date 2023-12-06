from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Question, QuizAttempt
import random


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('take_quiz')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('take_quiz')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def take_quiz(request):
    if request.method == 'POST':
        # Process the quiz submission
        questions = Question.objects.all()
        score = 0
        total_questions = len(questions)

        for question in questions:
            selected_choice = request.POST.get(str(question.id))
            if selected_choice:
                correct_choice = question.choices.get(is_correct=True)
                if str(correct_choice.id) == selected_choice:
                    score += 1

        percentage_score = (score / total_questions) * 100
        QuizAttempt.objects.create(user=request.user, score=percentage_score)

        return redirect('quiz_results')
    else:
        questions = list(Question.objects.all())
        if len(questions) >= 5:
            random_questions = random.sample(questions, 5)
        else:
            random_questions = questions

        return render(request, 'quiz.html', {'questions': random_questions})

@login_required
def quiz_results(request):
    user_attempts = QuizAttempt.objects.filter(user=request.user).order_by('-date_taken')
    return render(request, 'results.html', {'attempts': user_attempts})
