from django.contrib import admin
from django.urls import path, include

from base import urls as base
from restaurant import urls as restaurant
from accounts import urls as accounts


urlpatterns = [
    path('', include(base)),
    path('', include(restaurant)),
    path('', include(accounts)),

    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]
