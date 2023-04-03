from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect



def allow_base_groups(allow_role=[]):
    def decorator(view_func):
        def wrapped_func(request, *args, **kwargs):
            print('role:', allow_role)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allow_role:
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('/post/1')
        return wrapped_func
    return decorator