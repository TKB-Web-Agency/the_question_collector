from django.shortcuts import render
from django.views import generic
from .models import Question

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
