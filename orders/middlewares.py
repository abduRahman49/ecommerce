
class HeaderMiddleware:

    def __init__(self, get_response):
        # get_response correspond à la vue à exécuter par l'application
        self.get_response = get_response
    

    def __call__(self, request):
        # Traitement avant exécution de la vue
        print('Avant vue from middleware')
        response = self.get_response(request)  # get_response correspond à la vue
        # Traitement après exécution de la vue
        print('Après vue from middleware')
        return response
