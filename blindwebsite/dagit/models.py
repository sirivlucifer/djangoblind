from django.db import models
from ckeditor.fields import RichTextField #not so important because it's working.

# Create your models here.
class Kategori(models.Model):
    name = models.CharField(max_length=70)

class Gonderi(models.Model):
    title = models.CharField(max_length=255)
    #body = models.TextField() # rich olmayan text editör
    body = RichTextField(blank=True, null=True) # gayette rich olan text editör. çulsuz adam gereksiz adamdır.
    kategoriler = models.ManyToManyField('Kategori', related_name='gonderiler') #isimler dikkat

#ISIMLERE DIKKAT EDELIM! S LERE