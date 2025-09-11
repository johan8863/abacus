"""categories urls"""

# django
from django.urls import include, path

# third
from rest_framework import routers

# local
from apps.categories.api import endpoints

router = routers.DefaultRouter()
router.register(r'categories', endpoints.CategoryViewset, basename='cateories')


urlpatterns = [
    path('', include(router.urls)),
]
