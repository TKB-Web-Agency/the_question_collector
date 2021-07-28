from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Question, Categories
from accounts.models import CustomUser
from .forms import QuestionForm, CategoryForm
import datetime
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, 'home/homepage.html')

class Questions(generic.ListView):
    queryset = Question.objects.all()

    def get(self, request, *args, **kwargs):
        return super(generic.ListView, self).get(request, *args, **kwargs)

    template_name = 'home/homepage.html'

#class QuestionDetail(generic.DetailView):
#   model = Question
#
#    def get(self, request, *args, **kwargs):
#        return super(generic.DetailView, self).get(request, *args, **kwargs)
#
#    template_name = 'home/question_detail.html'

def filter(request, slug):
    category = Categories.objects.get(slug=slug)
    queryset = Question.objects.filter(categories=category.id)

    context = {
            'category': category.title,
            'question_list': queryset,
        }

    return render(request, 'home/homepage.html', context)

def question_detail(request, slug):
    question = get_object_or_404(Question, slug=slug)

    context = {
        'object': question,
        }

    return render(request, 'home/question_detail.html', context)



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

            new_item = Question.objects.create(title=question_title, slug=slug, submitted=user, date_created=datetime.datetime.now())
            new_item.categories.set(categories)
            new_item.save()
            return HttpResponseRedirect('/')

    else:
        form = QuestionForm()

    return render(request, 'home/add_new_question.html', {'form': form})

@login_required
def edit_question(request, pk):
    if request.method == 'GET':
        instance = get_object_or_404(Question, pk=pk)
        form = QuestionForm(instance=instance)
    else: 
        instance = get_object_or_404(Question, pk=pk)
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_title = form.cleaned_data['question']
            slug = slugify(question_title)
            categories = form.cleaned_data.get("categories")

            post = instance 
            post.title = question_title
            post.slug = slug
            post.submitted = request.user
            post.date_created = datetime.datetime.now()
            post.categories.set(categories)
            post.save()

        return HttpResponseRedirect('/')

    context = {
            'form': form,
            'instance': instance,
            'pk': pk,
            'url': 'edit'
            }
        
    return render(request, 'home/add_new_question.html', context)

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

##TODO: This shoud be done in react instead. Otherwise it will need to be rewritten. 
def report_question(request):
    return HttpResponseRedirect('/')
