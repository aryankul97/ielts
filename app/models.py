from django.db import models

class UserData(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	gender=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	phone=models.CharField(max_length=50)
	status=models.CharField(max_length=50)
	class Meta:
		db_table="UserData"
class EssayData(models.Model):
	userid=models.CharField(max_length=100)
	topic=models.CharField(max_length=100)
	essay=models.CharField(max_length=20000)
	wordcount=models.CharField(max_length=50)
	spellcheck=models.CharField(max_length=50)
	grammercheck=models.CharField(max_length=50)
	articlecheck=models.CharField(max_length=50)
	error=models.CharField(max_length=50)
	grade=models.CharField(max_length=50)
	totaltime=models.CharField(max_length=50)
	timetaken=models.CharField(max_length=50)
	class Meta:
		db_table="EssayData"
class HtmlData(models.Model):
	filename=models.CharField(max_length=100)
	code=models.CharField(max_length=10000)
	class Meta:
		db_table="HTMLData"
