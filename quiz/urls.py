from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('quiz/', views.take_quiz, name='take_quiz'),
    path('results/', views.quiz_results, name='quiz_results'),
    path('admin/', views.admin_page, name='admin_page'),
]
