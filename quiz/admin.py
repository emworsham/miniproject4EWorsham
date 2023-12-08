from django.contrib import admin
from .models import Question, Choice, QuizAttempt

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('short_title',)

    def short_title(self, obj):
        return obj.text[:25] + '...' if len(obj.text) > 25 else obj.text
    short_title.short_description = 'Question'

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(QuizAttempt)
