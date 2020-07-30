from django.db import models

class staff(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    mob = models.IntegerField()
    
    def __str__(self):
        return self.name

class routine(models.Model):
    subject = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.day) +" ("+ str(self.start_time) + ")"

class time(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title