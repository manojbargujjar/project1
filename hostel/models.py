# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from decimal import Decimal

class User(AbstractUser):
	phone=models.CharField(max_length=15, null=True , blank=True)
	fee_slip=models.CharField(max_length=25, null=True, blank=True)
	rank=models.CharField(max_length=20, null=True, blank=True)
	gender=models.CharField(max_length=20, null=True, blank=True)
	clas=models.CharField(max_length=30, null=True, blank=True)
	img=models.ImageField(upload_to='images' ,null=True, blank=True)
	

	def __str__(self):
		if self.username and self.clas and self.fee_slip:
			return self.username+ " " + self.clas+ " " + self.fee_slip
		return self.username
		
class Room(models.Model):
	usr= models.ForeignKey(User, on_delete=models.CASCADE)
	hname=models.CharField(max_length=50, null=True, blank=True)
	room_no=models.CharField(max_length=20, null=True, blank=True)
	block=models.CharField(max_length=20, null=True, blank=True)
	floor=models.CharField(max_length=20, null=True, blank=True)
	bed_no=models.CharField(max_length=20, null=True, blank=True)
	fees = models.DecimalField(max_digits=20, decimal_places=3, default=Decimal('0.000'))

	def __str__(self):
		return self.hname

class Complain(models.Model):
	usr=models.CharField(max_length=30, blank=True, null=True)
	room_no=models.CharField(max_length=10, blank=True, null=True)
	Complain=models.CharField(max_length=200, null=True, blank=True)
	date=models.DateTimeField(default=None, null=True)

	def __str__(self):
		return self.Complain

	

# Create your models here.
