from django.db import models

# Create your models here.
class Purchase_Model(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='images',blank=True,null=True)

    def __str__(self):
        return self.name