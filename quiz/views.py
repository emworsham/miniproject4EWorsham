from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Question, Choice, QuizAttempt
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
    questions = list(Question.objects.all())

    if request.method == 'POST':
        user_answers = {}
        score = 0

        for question in questions:
            selected_choice_id = request.POST.get(str(question.id))
            correct_choice = question.choices.get(is_correct=True)

            if selected_choice_id:
                selected_choice = question.choices.get(id=selected_choice_id)
                user_answers[question.id] = {
                    'question': question,
                    'selected': selected_choice,
                    'correct_choice': correct_choice,
                    'is_correct': selected_choice == correct_choice
                }
                if selected_choice == correct_choice:
                    score += 1

        percentage_score = (score / len(questions)) * 100
        QuizAttempt.objects.create(user=request.user, score=percentage_score)

        return render(request, 'quiz_results.html', {
            'user_answers': user_answers.values(),
            'score': percentage_score
        })

    random_questions = random.sample(questions, min(len(questions), 5))
    return render(request, 'quiz.html', {'questions': random_questions})

@login_required
def quiz_results(request):
    user_attempts = QuizAttempt.objects.filter(user=request.user).order_by('-date_taken')
    return render(request, 'results.html', {'attempts': user_attempts})
