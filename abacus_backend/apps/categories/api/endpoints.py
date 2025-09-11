"""endpoints from api categories module"""

# third
from rest_framework import viewsets

# local
from apps.categories.models import Category
from .serializers import CategorySeralizer


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySeralizer
    queryset = Category.objects.all()
