#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Income(models.Model):

    user = models.ForeignKey(User)
    item = models.CharField(max_length = 200, verbose_name = "Nazwa")
    amount = models.DecimalField(max_digits=8,decimal_places=2, verbose_name = "Kwota")
    date = models.DateField(verbose_name = "Data")


    def __unicode__(self):
        return self.item
