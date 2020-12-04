from django.db import models

# Create your models here.

class Config(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    #INSERT INTO "main"."ourconfig_config" ("title") VALUES ('HAKKIMIZDA');