from django.db import models

# Create your models here.

class Teacher(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=30)


class Student(models.Model):
    s_name = models.CharField(max_length=20)
    s_email = models.CharField(max_length=50)
    s_gender = models.CharField(max_length=10)
    s_phone = models.CharField(max_length=20)
    s_address = models.CharField(max_length=200)
    s_username = models.CharField(max_length=20)
    s_passwd = models.CharField(max_length=20)
