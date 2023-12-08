from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text[:50]} - {self.text}"

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(auto_now_add=True)
    score = models.FloatField()
    chosen_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)  # This line might be new or changed

    def __str__(self):
        return f"{self.user.username}'s attempt on {self.date_taken} with score: {self.score}"
