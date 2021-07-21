from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, UserUpdateForm
from .models import CustomUser

#Views Go Here
class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def profile(request, author):
    user = CustomUser.objects.get(username=author)

    context = {
        'author': user
        }

    return render(request, 'accounts/profile.html', context)


@login_required
def edit_profile(request, author):
    if request.method == 'GET':
        user = CustomUser.objects.get(username=author)
        form = UserUpdateForm(instance=request.user)
    else: 
        user = CustomUser.objects.get(username=author)
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['username']
            user.picture = form.cleaned_data['picture']
            user.website = form.cleaned_data['website']
            user.github = form.cleaned_data['github']
            user.about = form.cleaned_data['about']
            user.save()
        return redirect('accounts:profile', user.username)

    context = {
        'author': user,
        'form': form
        }

    return render(request, 'accounts/edit_profile.html', context)

