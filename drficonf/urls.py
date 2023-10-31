from django.contrib import admin
from django.urls import path, include, re_path
from wom.views import *
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/wom/', WomenAPIList.as_view()),
    path('api/v1/wom/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/wom_delete/<int:pk>/', WomenAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
