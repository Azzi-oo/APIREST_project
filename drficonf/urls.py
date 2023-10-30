from django.contrib import admin
from django.urls import path, include
from wom.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'wom', WomenViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/wom_list/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/wom_list/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    path('api/v1/', include(router.urls)),
]
