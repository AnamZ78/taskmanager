from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import DRFAuthGraphQLView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('tasks/', include('tasks.urls')),
    path('graphql/', csrf_exempt(DRFAuthGraphQLView.as_view(graphiql=True))),
]