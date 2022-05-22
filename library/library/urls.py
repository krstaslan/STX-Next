
from django import urls
from django.contrib import admin
from django.urls import path
from base.views import book_details,book_list,import_author,info


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',book_list, name="book_list"),
    path('',book_list, name="book_list"),
    path('book/<str:pk>', book_details, name="book_details"),
    path('import/',import_author, name="import_author"),
    path('api_spec/',info, name="info"),
 
    
]
# def BooksList(request):
#     author=request.GET.get('author') if request.GET.get('author') != None else ''
#     fromdate=request.GET.get('from') if request.GET.get('from') != None else ''
#     to=request.GET.get('to') if request.GET.get('to') != None else ''

#     acquired=request.GET.get('acquired') if request.GET.get('acquired') != None else ''
#     book=Book.objects.filter(
#         # Q(authors__icontains=[author]) |
#         Q(published_year__gt=fromdate) |
#         Q(published_year__lt=to) |
#         Q(acquired__icontains=acquired)       
#         )
#     serializer = BookSerializer(book , many=True)
#     return Response(serializer.data)