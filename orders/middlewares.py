
from django.http import HttpResponseForbidden


class HeaderMiddleware:

    def __init__(self, get_response):
        """Ceci est la méthode permettant d'inialiser la classe

        Args:
            get_response (view): Get response est la vue qui sera exécutée par le middleware
        """
        self.get_response = get_response
    

    def __call__(self, request):
        # Traitement avant exécution de la vue
        print('Avant vue from middleware')
        response = self.get_response(request)  # get_response correspond à la vue
        # Traitement après exécution de la vue
        print('Après vue from middleware')
        return response


class BlockScrapingToolsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request, *args, **kwargs):
        user_agent = request.META.get('HTTP_USER_AGENT')
        tools_to_block = ['PostmanRuntime/7.37.3', 'python-requests', 'Scrapy']
        if user_agent in tools_to_block:
            return HttpResponseForbidden('Agent non authorisé')
        
        return self.get_response(request, *args, **kwargs)
