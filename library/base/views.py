from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book,Import
from .serializers import ImportSerializer, BookSerializer,DataSerializer
import requests,json
from .booksave import BookSave
from django.http import HttpResponse
from django.db.models import Q
from django.db.models.functions import Cast
from django.db.models import IntegerField, CharField
@api_view(['GET','POST'])
def book_list(request):
    if request.method =="GET":
        try:
               
            auth=str(request.GET.get('author')) 
            author=auth[1:-1]
            acquir=request.GET.get('acquired') if request.GET.get('acquired') != None else ''
            fromdate=int(request.GET.get('from')) 
            to=int(request.GET.get('to')) if request.GET.get('to') != None else ''
            print(acquir)
            book=Book.objects.annotate(
                published_year_integer=Cast('published_year', output_field=IntegerField()),
                authors_as_string=Cast('authors', output_field=CharField(max_length=200))).filter(
                Q(acquired__icontains=acquir),
                Q(published_year_integer__lte=to),
                Q(published_year_integer__gte=fromdate),
                Q(authors__icontains= author)
                )
            serializer = BookSerializer(book , many=True)
            return Response(serializer.data)
        except:
            books= Book.objects.all()
            serializer = BookSerializer(books , many=True)
            return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PATCH','DELETE'])
def book_details(request,pk):
    try:
        book= Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=BookSerializer(book)
        return Response(serializer.data)

    elif request.method == "PATCH":
        data=request.data
        serializer=BookSerializer(book,data=request.data)
        #print(data["id"])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)           
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def import_author(request):
    if request.method =="GET":
        author= Import.objects.all()
        serializer = ImportSerializer(author , many=True)
        return Response(serializer.data)    
    elif request.method == "POST":
        data=request.data
        serializer = ImportSerializer(data=request.data)
        if serializer.is_valid():
            auth=request.POST.get("authors")
            try:
                response = requests.get(url="https://www.googleapis.com/books/v1/volumes?q=inauthor={auth}")
            except:
                response.raise_for_status()
            api_data = response.json()
            items=api_data["items"]
            BookSave(items)
            imported =len(items)
            mydata2={"imported": imported}          
            serializer = DataSerializer(data=mydata2)
            if serializer.is_valid():
                return Response(serializer.data)
def info(request):
    my_json = json.dumps({"info": {"version": "2022.05.16"}})
    return HttpResponse(my_json)


