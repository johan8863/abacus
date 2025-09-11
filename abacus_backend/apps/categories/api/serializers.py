"""serializers from api categories module"""

# third
from rest_framework import serializers

# local
from apps.categories.models import Category


class CategorySeralizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
