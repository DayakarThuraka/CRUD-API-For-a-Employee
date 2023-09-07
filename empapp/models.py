from django.db import models

# Create your models here.
class EmpData(models.Model):
    emp_name=models.CharField(max_length=100)
    domain=models.CharField(max_length=50)
    experiance=models.CharField(max_length=20)
    salary=models.BigIntegerField(default='')
    location=models.CharField(max_length=50)

    def __str__(self):
        return self.emp_name