from django.contrib import admin
from django.urls import path, include
from apps.userauth.urls import urlpatterns as auth_urls
from apps.users.urls import urlpatterns as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include(auth_urls)),
    path('api/v1/users/', include(user_urls)),
]
