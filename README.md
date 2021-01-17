# DRF Question

I closely followed the tutorial at: https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners

All goes well until I arrive at the chapter: Root API Endpoint

After updating the views.py with the reverse() functions, I end up with the error: `Reverse for 'user-list' not found. 'user-list' is not a valid view function or pattern name.`


The question: How to fix this error?

To reproduce:

- clone the repository
- create a virtual environment: `python -m venv venv`
- activate the virtual environment: `source venv/bin/activate`
- run the server:
  - `python manage.py makemigrations snippets`
  - `python manage.py createsuperuser`
  - `python manage.py runserver`
- add some snippets
- try to the the list of snippets: http://127.0.0.1:8000/

The error message:
```
Django version 3.1.5, using settings 'tutorial.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Internal Server Error: /
Traceback (most recent call last):
  File "/home/patrick/Projects/temp/drf/venv/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/home/patrick/Projects/temp/drf/venv/lib/python3.9/site-packages/django/core/handlers/base.py", line 181, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/patrick/Projects/temp/drf/venv/lib/python3.9/site-packages/django/views/decorators/csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "/home/patrick/Projects/temp/drf/venv/lib/python3.9/site-packages/django/views/generic/base.py", line 70, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/patrick/Projects/temp/drf/venv/lib/python3.9/site-packages/rest_framework/views.py", line 509, in dispatch
    response = self.handle_exception(exc)
  File "/home/patrick/Projects/temp/drf/venv/lib/python3.9/site-packages/rest_framework/views.py", line 469, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/patrick/Projects/temp/drf/venv/lib/python3.9/site-packages/rest_framework/views.py", line 480, in raise_uncaught_exception
    raise exc
  File "/home/patrick/Projects/temp/drf/venv/lib/python3.9/site-packages/rest_framework/views.py", line 506, in dispatch
    response = handler(request, *args, **kwargs)
  File "/home/patrick/Projects/temp/drf/venv/lib/python3.9/site-packages/rest_framework/decorators.py", line 50, in handler
    return func(*args, **kwargs)
  File "/home/patrick/Projects/temp/drf/snippets/views.py", line 16, in api_root
    'users': reverse('user-list', request=request, format=format),
  File "/home/patrick/Projects/temp/drf/venv/lib/python3.9/site-packages/rest_framework/reverse.py", line 47, in reverse
    url = _reverse(viewname, args, kwargs, request, format, **extra)
  File "/home/patrick/Projects/temp/drf/venv/lib/python3.9/site-packages/rest_framework/reverse.py", line 60, in _reverse
    url = django_reverse(viewname, args=args, kwargs=kwargs, **extra)
  File "/home/patrick/Projects/temp/drf/venv/lib/python3.9/site-packages/django/urls/base.py", line 87, in reverse
    return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))
  File "/home/patrick/Projects/temp/drf/venv/lib/python3.9/site-packages/django/urls/resolvers.py", line 685, in _reverse_with_prefix
    raise NoReverseMatch(msg)
django.urls.exceptions.NoReverseMatch: Reverse for 'user-list' not found. 'user-list' is not a valid view function or pattern name.
[17/Jan/2021 13:57:07] "GET / HTTP/1.1" 500 112189
```

I started this tutorial because I have the exact same problem in another project. I was hoping to learn in the tutorial what I did wrong.

So I am at a loss for how to get this to work...


~~ Patrick


PS. As far as I can tell, this is the official Django Rest Framework tutorial.
PS2. I have asked this question on Reddit: https://www.reddit.com/r/djangolearning/comments/kz7pe2/reverse_does_not_work_in_django_rest_framework/
