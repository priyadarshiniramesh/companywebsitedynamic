from django.db import models
from django.contrib import admin
# Create your models here.

class people(models.Model):
    Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')

class peopleadmin(admin.ModelAdmin):
    list_display = ('Name','Designation','photo' )


class product(models.Model):
    Name = models.CharField(max_length=100)
    Price  = models.IntegerField()
    photos = models.ImageField(upload_to='photoss/')

class productadmin(admin.ModelAdmin):
    list_display = ('Name','Price','photos' )


