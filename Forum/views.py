from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm  # DJANGO BUILT IN FORM
from.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout  #AUTHENTICATION FROM DJANGO
from django.contrib.auth.decorators import login_required


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
def home(request):
    context = {
        'questions': questions
    }

    return render(request, 'forum/home.html', context)


def register(request):
    if request.user.is_authenticated:   #ENSURE LOGGED IN USERS CANT ACCESS THIS AREA
        return redirect('forum-home')
    else:
        form = CreateUserForm  #GENERATING AUTO GENERATED FORM WE ADD TO THIS LATER
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account' + user + 'created')
                return redirect('login')
    context = { 'form':form }
    return render(request, 'forum/register.html', context)


def loginpage(request):
    if request.user.is_authenticated:   #ENSURE LOGGED IN USERS CANT ACCESS THIS AREA
        return redirect('forum-home')
    else:
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