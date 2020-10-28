from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm  # DJANGO BUILT IN FORM
from.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout  #AUTHENTICATION FROM DJANGO
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users


questions = [
    {
        'author': 'Hamad Kashmiri',
        'title': 'Question1',
        'content':  'question content',
        'date':     'august 28, 2018'
    },
    {
        'author': 'Hamad Kashmiri',
        'title': 'Question2',
        'content':  'question content',
        'date':     'august 28, 2018'
    }
]
@login_required(login_url='login')   #DECORATOR PROTECTS PAGES FROM UNAUTHORISED USERS
@allowed_users(allowed_roles='admin') #PROTECTS PAGES BASED ON USER ROLES
def home(request):
    context = {
        'questions': questions
    }

    return render(request, 'forum/home.html', context)

@unauthenticated_user
def register(request):
    form = CreateUserForm  #GENERATING AUTO GENERATED FORM WE ADD TO THIS LATER
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='users')
            user.groups.add(group)
            messages.success(request, 'Account ' + username + ' created')
            return redirect('login')
    context = { 'form':form }
    return render(request, 'forum/register.html', context)


@unauthenticated_user
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)   #AUTHENTICATING USER USING AUTHENTICATE LIB (CHECKS AGAINST DATABASE VALUES)
        
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'username or password is incorrect') # WE DONT EXPLICITLY SAY WHICH IS INCORRECT SO HACKERS DONT HAVE ANY EXTRA INFORMATION

    context = {}
    return render(request, 'forum/login.html', context)

def logoutUser(request):
    context = {}
    logout(request)

    return render(request, 'forum/logout.html', context)

@login_required(login_url='login')
def profile(request):
    context = {
        
    }

    return render(request, 'forum/profile.html', context)