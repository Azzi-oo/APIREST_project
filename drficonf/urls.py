from django.contrib import admin
from django.urls import path
from wom.views import WomenAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/wom_list/', WomenAPIView.as_view()),
]
