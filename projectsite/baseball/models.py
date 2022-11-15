from django.db import models

# Create your models here.
class Person(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=5, null=True)

    def __str__(self):
        return "Person{lastname=%s, firstname=%s, height=%s, weight=%s}" % (self.lastname, self.firstname, self.height, self.weight)
