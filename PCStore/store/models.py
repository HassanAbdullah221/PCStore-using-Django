from django.db import models
from datetime import datetime
from django.contrib.contenttypes.fields import GenericForeignKey


class PC(models.Model):
    name = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    gpu = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)       
    storage = models.CharField(max_length=100)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, default='PC')
    image = models.ImageField(upload_to="pc/" , default='images/1.jpeg')

class Monitor(models.Model):
    name = models.CharField(max_length=100)
    size_in_inches = models.FloatField()  
    resolution = models.CharField(max_length=50) 
    refresh_rate = models.IntegerField()  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, default='Monitor')

    image = models.ImageField(upload_to="monitor/", default='images/1.jpeg')

class Mouse(models.Model):
   
    name = models.CharField(max_length=100)
    dpi = models.IntegerField()
    connection_type = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, default='Mouse')
    image = models.ImageField(upload_to='mice/')

class Chair(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=20)
    adjustable = models.CharField(max_length=3)
    max_weight = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, default='Chair')

    image = models.ImageField(upload_to='gaming_chairs/')
    
class Headset(models.Model):
    
    name = models.CharField(max_length=100)
    connection_type = models.CharField(max_length=20)
    has_microphone = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, default='Headset')

    image = models.ImageField(upload_to='headsets/')


class Keyboard(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, default='Keyboard')
    image = models.ImageField(upload_to='keyboards/')


class PC_comment(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Monitor_comment(models.Model):
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Mouse_comment(models.Model):
    mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Chair_comment(models.Model):
    chair = models.ForeignKey(Chair, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Headset_comment(models.Model):
    headset = models.ForeignKey(Headset, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Keyboard_comment(models.Model):
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


