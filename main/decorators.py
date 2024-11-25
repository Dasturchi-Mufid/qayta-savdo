from django.shortcuts import redirect
from functools import wraps

def login_required_session(view_func):
    """
    Decorator to check if the session has a 'user' key. If not, redirect to the login page.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        
        if not request.session.get('user', None):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view