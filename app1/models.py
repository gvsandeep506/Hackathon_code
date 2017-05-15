# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.




class Department(models.Model):
	name = models.CharField(max_length=128)

	def __unicode__(self):
		return self.name


class userInfo(models.Model):
	userName = models.CharField(max_length=20)
	userFirstName = models.CharField(max_length=20)
	userLastName = models.CharField(max_length=20)
	phoneNumber = models.CharField(max_length=15)
	email = models.EmailField()
	department = models.CharField(max_length=128)


class certificateInfo(models.Model):
	certName = models.CharField(max_length=128)
	certType = models.CharField(max_length=128)
	certPasswd = models.CharField(max_length=500)
	expiryDate = models.CharField(max_length=20)
	department = models.CharField(max_length=128)
	primaryOwner = models.CharField(max_length=128)
	secondaryOwners = models.CharField(max_length=128)
	escalationMail = models.EmailField()
	reminderDays = models.CharField(max_length=5)
	comment = models.CharField(max_length=300)


class certificateType(models.Model):
	certType = models.CharField(max_length=128)


class departmentInfo(models.Model):
	departmentName = models.CharField(max_length=128)










