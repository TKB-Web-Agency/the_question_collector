from django.contrib import admin
from .models import Question, Categories

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Categories, CategoriesAdmin)
