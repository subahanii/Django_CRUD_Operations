from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=30)
    ename=models.CharField(max_length=100)
    epass = models.CharField(max_length=100,default='default')
    email=models.EmailField()
    eimg = models.FileField(upload_to='app/img')
    econtact=models.CharField(max_length=15)

    class Meta:
        db_table= "employee"



