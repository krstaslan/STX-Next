
from warnings import filters
import django_filters
from .models import Book
from django.db.models import Q

class BookFilter(django_filters.FilterSet):
    class Meta:
        model=Book 
        fields={
            'title':['icontains'],
            'acquired':['icontains'],
        }

    def my_lookup_method(self, queryset, name, value):
        return queryset.filter(Q(title__icontains=value)|Q(virtual_ip__icontains=value))
            #   'from':['published_year__gt'],
            # 'to':['published_year__lt'],      
        #('title','to','from','acquired')


# class BookFilter(django_filters.FilterSet):
#     to = DateFilter(field_name='published_year')
#     fromm = DateFilter(field_name='published_year')
#     class Meta:
#         model =Book
#         fields='__all__'