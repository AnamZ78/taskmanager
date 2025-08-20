from graphene_django.views import GraphQLView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser

class DRFAuthGraphQLView(GraphQLView):
    def parse_body(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', '')
        if auth.startswith('Token '):
            token_key = auth.split(' ')[1]
            try:
                token = Token.objects.get(key=token_key)
                request.user = token.user
            except Token.DoesNotExist:
                request.user = AnonymousUser()
        return super().parse_body(request)