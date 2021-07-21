from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Question, Categories
from accounts.models import CustomUser
from .forms import QuestionForm, CategoryForm
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
            categories = form.cleaned_data.get("categories")

            if request.user.is_authenticated:
                user = request.user
            else:
                user = CustomUser.objects.get(uuid='bfd9134b-30f7-4645-9184-805084758b9c')

            new_item = Question.objects.create(title=question_title, slug=slug, author=user, date_created=datetime.datetime.now())
            new_item.categories.set(categories)
            new_item.save()
            return HttpResponseRedirect('/')

    else:
        form = QuestionForm()

    return render(request, 'home/add_new_question.html', {'form': form})

def add_new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category_title = form.cleaned_data['category']
            slug = slugify(category_title)
            
            #Create new category object
            new_category = Categories.objects.create(title=category_title, slug=slug)
            new_category.save()
            return redirect('home:add_new_question')

    else:
        form = CategoryForm()

    return render(request, 'home/add_new_category.html', {'form': form})

