import django_filters

from .models import *

class BookFilter(django_filters.FilterSet):
    book_title = django_filters.CharFilter(lookup_expr='icontains')
    book_author = django_filters.CharFilter(lookup_expr='icontains')
    book_type = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['book_title','book_author', 'book_published', 'book_pages', 'book_type',] 