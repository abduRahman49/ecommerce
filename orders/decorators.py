from django.http import HttpResponseForbidden


def decorator(func):
    def wrapper(request, *args, **kwargs):
        # Traitement avant exécution de la vue
        print('Avant vu from decorateur')
        response = func(request, *args, **kwargs)
        # Traitement après exécution de la vue
        print('Après vue from decorateur')
        return response
    return wrapper


def is_user_authenticated(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('User is not authenticated')
        
        return func(request, *args, **kwargs)
    
    return wrapper
