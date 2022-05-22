from django.contrib import admin
from django.urls import path
from base.views import book_details,book_list,import_author,info


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',book_list, name="book_list"),
    path('book',book_list, name="book_list"),
    path('',book_list, name="book_list"),
    path('book/<str:pk>', book_details, name="book_details"),
    path('import/',import_author, name="import_author"),
    path('api_spec/',info, name="info"),
 
    
]
