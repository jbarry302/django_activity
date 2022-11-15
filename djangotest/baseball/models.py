from django.db import models

# Create your models here.
class Person(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    height = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=5, null=True)

    def get_lastname(self):
        return self.lastname
    
    def get_firstname(self):
        return self.firstname
    
    def get_height(self):
        return self.height
    
    def get_weight(self):
        return self.weight

    def __str__(self) -> str:
        return "Person{lastname=%s, firstname=%s, height=%s, weight=%s}" % (self.lastname, self.firstname, self.height, self.weight)
