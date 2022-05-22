
from rest_framework.serializers import ModelSerializer
from .models import Book,Import,Data

class BookSerializer(ModelSerializer):
    class Meta:
        model= Book
        fields='__all__'

class ImportSerializer(ModelSerializer):
    class Meta:
        model= Import
        fields=['authors']

class DataSerializer(ModelSerializer):
    class Meta:
        model= Data
        fields=['imported']

