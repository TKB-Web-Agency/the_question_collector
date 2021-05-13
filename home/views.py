from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Question
from .forms import QuestionForm
import datetime
from django.utils.text import slugify

# Create your views here.
def homepage(request):
    return render(request, 'home/homepage.html')

class Questions(generic.ListView):
    queryset = Question.objects.all()

    def get(self, request, *args, **kwargs):
        return super(generic.ListView, self).get(request, *args, **kwargs)

    template_name = 'home/homepage.html'

class QuestionDetail(generic.DetailView):
    model = Question

    def get(self, request, *args, **kwargs):
        return super(generic.DetailView, self).get(request, *args, **kwargs)

    template_name = 'home/question_detail.html'

def add_new_question(request):
    if request.method == 'POST':
        form =  QuestionForm(request.POST)
        if form.is_valid():
            question_title = form.cleaned_data['question']
            slug = slugify(question_title)
            new_item = Question.objects.create(title=question_title, slug=slug, date_created=datetime.datetime.now())
            new_item.save()
            print(new_item)
            return HttpResponseRedirect('/')

    else:
        form = QuestionForm()

    return render(request, 'home/add_new_question.html', {'form': form})


