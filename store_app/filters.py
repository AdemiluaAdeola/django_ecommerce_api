from django_filters.rest_framework import FilterSet
from store_app.models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category_id': ['exact'],
            'price': ['gt', 'lt']
        }