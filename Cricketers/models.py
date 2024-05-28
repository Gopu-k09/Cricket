from django.db import models

# Create your models here.


class Cricketer(models.Model):
    name=models.CharField(max_length=120,null=False)
    age=models.IntegerField(null=True)
    country=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name

