'''This file writes decorators to restrict access based on user roles'''

from django.http import HttpResponse
from django.shortcuts import redirect   

def unauthenticated_user(view_func):        #called when used in views
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:   #ENSURE LOGGED IN USERS CANT ACCESS THIS AREA
            return redirect('forum-home')   #REDIRECT THEM TO CORRECT PAGE
        else:       
            return view_func(request, *args, **kwargs)  #RUN THE ORIGINAL VIEW FUNCTION IF THE CONDITIONAL IS NOT MET
    
    return wrapper_func

    #decorator takes a func as param and adds extra functionality before the original function is called

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None    # SETS UP GROUP VAR
            if request.user.groups.exists():        #CHECKS IF GROUP EXISTS
                group = request.user.groups.all()[0].name  # GETS THE NAME OF THE GROUP BELONGING TO THE USER
            if group in allowed_roles:  
                return view_func(request, *args, **kwargs)  # RUN VIEW FUNCTION IF ALLOWED
            else:
                return HttpResponse('unauthorized to view the page')    #DISPLAY MESSAGE IF NOT
        return wrapper_func
    return decorator