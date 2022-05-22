from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField
class Book(models.Model):
    external_id = models.CharField(max_length=200, null=True)
    title= models.CharField(max_length=200, null=True)
    authors=ArrayField(models.CharField(max_length=200), blank=True)
    published_year = models.IntegerField(default=datetime.datetime.now().year)
    acquired=models.BooleanField(default=False)
    thumbnail=models.CharField(max_length=400,null=True)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=('title',)
    
class Import(models.Model):
    authors = models.CharField(max_length=200) 
    def __str__(self):
        return self.authors

class Data(models.Model):
    imported=models.IntegerField(default=0,null=True)
    def __str__(self):
        return self.imported
