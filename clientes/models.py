from django.db import models

class Documento(models.Model):
    num_doc = models.CharField(max_length=30)

    def __str__(self):
        return self.num_doc



class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photo', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'