from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(label='Add a new question', max_length=280)

