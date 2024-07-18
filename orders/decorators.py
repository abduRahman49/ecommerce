
def decorator(func):
    def wrapper(request, *args, **kwargs):
        # Traitement avant exécution de la vue
        print('Avant vu from decorateur')
        response = func(request, *args, **kwargs)
        # Traitement après exécution de la vue
        print('Après vue from decorateur')
        return response
    return wrapper
