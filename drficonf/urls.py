from django.contrib import admin
from django.urls import path
from wom.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/wom_list/', WomenAPIList.as_view()),
    path('api/v1/wom_list/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/wom_detail/<int:pk>/', WomenAPIDetailView.as_view()),
]
