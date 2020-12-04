from django.db import models

# Create your models here.
class Kategori(models.Model):
    name = models.CharField(max_length=70)

class Gonderi(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    kategoriler = models.ManyToManyField('Kategori', related_name='gonderiler') #isimler dikkat

#ISIMLERE DIKKAT EDELIM! S LERE