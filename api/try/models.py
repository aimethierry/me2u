# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class client(models.Model):
    compony = models.ForeignKey('compony', null=True)
    

    def __str__(self):
        return str(self.compony)

class compony(models.Model):
    name_of_compony = models.CharField(max_length=140, null=True)
    adress = models.CharField(max_length=140, null=True)
    location = models.CharField(max_length=140, null=True)

    def __str__(self):
        return self.name_of_compony


class users(models.Model):
    user = models.ForeignKey(User, null=True)
    compony = models.ManyToManyField('compony', null=True)
    first_name = models.CharField(max_length=140, null=True)
    last_name = models.CharField(max_length=140, null=True)
    amount = models.IntegerField()   

    def __str__(self):
        return self.first_name 


    

