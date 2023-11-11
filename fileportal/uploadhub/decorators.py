# decorators.py
from functools import wraps
from django.conf import settings
from django.shortcuts import render, redirect

def password_protected_view(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.method == 'POST' and 'password' in request.POST:
            if request.POST['password'] == settings.UPLOADHUB_PASSWORD:
                request.session['authenticated'] = True
            else:
                return render(request, 'password_entry.html', {'error': 'Incorrect password.'})

        if not request.session.get('authenticated', False):
            return render(request, 'password_entry.html')
        
        return function(request, *args, **kwargs)
    
    return wrap
