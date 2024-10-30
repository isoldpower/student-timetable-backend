from django.contrib import admin
from django.urls import path, include
from apps.userauth.urls import urlpatterns as auth_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include(auth_urls)),
]
