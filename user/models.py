from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
class CustomUser(AbstractUser):
    number = models.CharField(blank=True, null=True,max_length=13,verbose_name='Номер телефона ')
    kode = models.CharField(blank=True,null=True,max_length=3,verbose_name="Code of operator") # Kode of number field 
    #TODO: if it mts or another operator we need to send kode TODO in views.py
class NewsLetter(models.Model):
    id = models.AutoField(primary_key=True)
    gets = CustomUser.objects.values('kode').distinct()
    
    CHOISE_NUMBER = [(item['kode'], item['kode']) for item in gets]
    created = models.DateTimeField()
    filternumber = models.CharField(max_length=3, choices=CHOISE_NUMBER,null=True)
    title = models.CharField(blank=True,max_length=32,verbose_name="Name",help_text='Name of NewsLetter',)
    messages = models.TextField(blank=True, null=False, max_length=255)
    finished = models.DateTimeField()
    def __str__(self):
        return self.title
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name="When message was created")
    Status = models.BooleanField(help_text="True = Send,False = NOT",verbose_name='Status')
    idras = models.OneToOneField(NewsLetter,on_delete=models.CASCADE) # TODO: id рассылки
    idclients = models.ManyToManyField('CustomUser')