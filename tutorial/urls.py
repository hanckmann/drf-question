from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.api_root),
    path('', include('accounts.urls')),
    path('', include('snippets.urls')),
]
