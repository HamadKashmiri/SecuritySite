from django.shortcuts import render
from django.http import HttpResponse

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

def home(request):
    context = {
        'questions': questions
    }

    return render(request, 'forum/home.html', context)