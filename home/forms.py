from django import forms
from .models import Question, Categories

class QuestionForm(forms.ModelForm):
    question = forms.CharField(widget=forms.Textarea(), required=True, label=False) 
    categories = forms.ModelMultipleChoiceField(queryset=Categories.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Question
        fields = ('question', 'categories')

class CategoryForm(forms.Form):
    category = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ''}), required=True, label=False) 

