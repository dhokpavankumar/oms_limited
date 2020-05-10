from django.db import models




class student(models.Model):
    name=models.CharField(max_length=100)
    mobile_number=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    userID=models.CharField(max_length=50)







