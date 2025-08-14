from django.db import models

# Create your models here.
"""Create a model representing a company with departments
 and employees, using ForeignKey relationships"""

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employee')

    def __str__(self):
        return self.name