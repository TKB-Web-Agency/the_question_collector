from django import forms
from .models import Categories

class QuestionForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ''}), required=True, label=False) 
    categories = forms.ModelMultipleChoiceField(queryset=Categories.objects.all(), widget=forms.CheckboxSelectMultiple)

