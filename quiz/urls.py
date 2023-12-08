from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # The main page of your quiz app
    path('register/', views.register, name='register'),  # For user registration
    path('login/', views.login, name='login'),  # For user login
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('quiz/', views.take_quiz, name='take_quiz'),  # To take a quiz
    path('results/', views.quiz_results, name='quiz_results'),  # To view quiz results
    # Add other URL patterns here as needed
]

