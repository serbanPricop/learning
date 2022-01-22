import re
from django.shortcuts import render
from datacamp_app.forms import TopicForm, WebPageForm, UserProfileInfoForm, UserForm
from datacamp_app.models import WebPage
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def index(request):
    return render(request, 'datacamp_app/base.html')


def page(request):

    if request.method == 'POST':
        form = WebPageForm(request.POST)

        if form.is_valid():
            topic = form.cleaned_data['topic']
            name = form.cleaned_data['name']
            url = form.cleaned_data['url']

            webPage = WebPage(topic=topic, name=name, url=url)
            webPage.save()

            return HttpResponseRedirect('/datacamp/')
    else:
        form = WebPageForm()

    return render(request, 'datacamp_app/page.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('You are logged in')

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")
        else:
            print('Someone tried to login and failed',username, password)
            return HttpResponse('Invalid credentials')
    else:
        return render(request,'datacamp_app/login.html',{})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save() 

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()

            registered = True

            return HttpResponseRedirect('/')

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'datacamp_app/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })
