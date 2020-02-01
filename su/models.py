from __future__ import unicode_literals
from django.db import models
import os
from datetime import datetime,date
from django import forms
from django.contrib.auth.models import User
import uuid
from django.db import models
from django import forms
#from django.contrib.admin.widgets import AdminDateWidget



def content_album_name(instance, filename):
	return os.path.join(instance.name,filename)
def content_album_name2(instance, filename):
	return os.path.join(instance.gm_id.name,filename)
#######Use verbose name


class Coord(models.Model):
	stype=(('Active','Active'),('Inactive','Inactive'))
	user = models.OneToOneField(User)
	cg_id= models.UUIDField("Coordinator UUID",primary_key=True, default=uuid.uuid4, editable=False)
	cg_name = models.CharField("Coordinator Name",max_length=32,blank=False)
	cg_bitsid = models.CharField("Coordinator Bits ID (without a 'P')",max_length=32, unique=False)
	assoc_name = models.CharField("Association",max_length=64, blank=False)
	status=models.CharField(choices=stype,max_length=32,default='Active')
	date = models.DateTimeField(auto_now=True)
	reg_by = models.CharField(max_length=32)
	def __str__(self):
		return self.cg_name


class Wear(models.Model):
	mtype=(('T Shirt','T Shirt'),('Sweat Shirt','Sweat Shirt'),('Other','Other'))
	stype=(('Active','Active'),('Inactive','Inactive'))
	emtype=(('Sent','Sent'),('Not Sent','Not Sent'))
	gm_id=  models.UUIDField("Wear UUID",primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField("Merchandise Name",max_length=32)
	meal= models.CharField("Merchandise Type",choices=mtype,max_length=32,default='T Shirt')
	cg_id= models.ForeignKey(Coord,verbose_name="Coordinator Id")
	reg_date = models.DateTimeField("End of Signing & Cancellation Process",default=datetime.now, blank=False)
	date = models.DateField(default=datetime.now,blank=False)
	deadline = models.DateField(default=datetime.now,blank=False)
	deadline2 = models.DateField(default=datetime.now,blank=False)
	status=models.CharField(choices=stype,max_length=128,default='Active')
	excel = models.FileField(upload_to=content_album_name,blank=True)
	mails=models.CharField(choices=emtype,max_length=128,default='Not Sent',blank=False)
	image =  models.ImageField("Merchandise image",upload_to=content_album_name, blank=False)
	price = models.IntegerField("Merchandise Price",default=0,null=False)
	def __str__(self):
		return self.name



class Wear_Student(models.Model):
	unique_id = models.UUIDField("Unique Student Id",primary_key=True, default=uuid.uuid4, editable=False)
	stype=(('Signed Up','Signed Up'),('Opted Out','Opted Out'))
	mtype=(('S','S'),('M','M'),('L','L'),('XL','XL'),('XXL','XXL'), ('XXXL','XXXL'))
	emtype=(('Sent','Sent'),('Not Sent','Not Sent'))
	name = models.CharField(max_length=32)
	student_id= models.CharField("Bits Id",max_length=32,blank=False)
	user_id=models.CharField("Bits Email Id",db_index=True,max_length=64,blank=False)
	gm_id = models.ForeignKey(Wear,default='1',verbose_name="Wear Id")
	mail=models.CharField(choices=emtype,max_length=128,default='Not Sent',blank=False)
	meal= models.CharField("Size Selected",choices=mtype,max_length=16,default='S',blank=False)
	status=models.CharField(choices=stype,max_length=128,blank=False)
	room=models.CharField("Room No.",max_length=32,default='4126')
	bhawan=models.CharField("Bhawan",max_length=32,default='BD')
	price = models.IntegerField("Price",default=0,null=False)
	class Meta:
		unique_together = ('student_id', 'gm_id','status')
	def __str__(self):
                return self.student_id

class Event(models.Model):
	mtype=(('Workshop/FoodStall','Workshop/FoodStall'),('Prof Show','Prof Show'))
	stype=(('Active','Active'),('Inactive','Inactive'))
	emtype=(('Sent','Sent'),('Not Sent','Not Sent'))
	gm_id=  models.UUIDField("Event UUID",primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField("Event Name",max_length=32)
	meal= models.CharField("Event Type",choices=mtype,max_length=32,default='Workshop/FoodStall')
	cg_id= models.ForeignKey(Coord,verbose_name="Coordinator Id")
	reg_date = models.DateTimeField("End of Signing & Cancellation Process",default=datetime.now, blank=False)
	date = models.DateField(default=datetime.now,blank=False)
	deadline = models.DateField(default=datetime.now,blank=False)
	deadline2 = models.DateField(default=datetime.now,blank=False)
	status=models.CharField(choices=stype,max_length=128,default='Active')
	excel = models.FileField(upload_to=content_album_name,blank=True)
	mails=models.CharField(choices=emtype,max_length=128,default='Not Sent',blank=False)
	image =  models.ImageField("Event image",upload_to=content_album_name, blank=False)
	venue =  models.CharField("Event Venue",max_length=16,blank=False)
	price = models.IntegerField("Event Price",default=0,null=True)
	def __str__(self):
		return self.name



class Event_Student(models.Model):
	unique_id = models.UUIDField("Unique Student Id",primary_key=True, default=uuid.uuid4, editable=False)
	stype=(('Signed Up','Signed Up'),('Opted Out','Opted Out'))
	emtype=(('Sent','Sent'),('Not Sent','Not Sent'))
	mtype=(('Workshop/FoodStall','Workshop/FoodStall'),('Prof Shows','Prof Shows'))
	name = models.CharField(max_length=64)
	student_id= models.CharField("Bits Id",max_length=32,blank=False)
	user_id=models.CharField("Bits Email Id",db_index=True,max_length=40,blank=False)
	gm_id = models.ForeignKey(Event,default='1',verbose_name="Event Id")
	mail=models.CharField(choices=emtype,max_length=128,default='Not Sent',blank=False)
	meal= models.CharField("Event Selected",choices=mtype,max_length=16,default='Workshop/FoodStall',blank=True)
	status=models.CharField(choices=stype,max_length=128,blank=False)
	room=models.CharField("Room No.",max_length=32,default='4126')
	bhawan=models.CharField("Bhawan",max_length=32,default='BD')
	price = models.IntegerField("Price",default=0,null=True)
	class Meta:
		unique_together = ('student_id', 'gm_id','status')
	def __str__(self):
                return self.student_id

class Student(models.Model):
	unique_id = models.UUIDField("Unique Stud Id",primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=64)
	bits_id= models.CharField("BITS ID",max_length=64,unique=False) # earlier true
	bhawan = models.CharField(max_length=32)
	room_no = models.CharField("Room No.",max_length=4)
	user_id=models.CharField("Bits Email Id",db_index=True,max_length=64,blank=False)
	def __str__(self):
                return self.user_id


class DateMailStatus(models.Model):
	date = models.DateField(default=datetime.now,blank=False)
	mails = models.IntegerField("Mails Sent",default = 0)
	def __str__(self):
		return self.date.strftime('%m/%d/%Y')


class Wear_Invalid_Students(models.Model):
	mtype=(('T Shirt','T Shirt'),('Sweat Shirt','Sweat Shirt'),('Other','Other'))
	student_id= models.CharField("Bits Id",max_length=32,blank=False)
	gm_id = models.ForeignKey(Wear,default='1',verbose_name="Wear Id")
	meal= models.CharField("Type Selected",choices=mtype,max_length=16,default='T Shirt',blank=False)
	class Meta:
		unique_together = ('student_id', 'gm_id')
	def __str__(self):
		return self.student_id

class Event_Invalid_Students(models.Model):
	mtype=(('Workshop/FoodStall','Workshop/FoodStall'),('Prof Shows','Prof Shows'))
	student_id= models.CharField("Bits Id",max_length=32,blank=False)
	gm_id = models.ForeignKey(Event,default='1',verbose_name="Event Id")
	meal= models.CharField("Type Selected",choices=mtype,max_length=32,default='Workshop/FoodStall',blank=False)
	class Meta:
		unique_together = ('student_id', 'gm_id')
	def __str__(self):
		return self.student_id
