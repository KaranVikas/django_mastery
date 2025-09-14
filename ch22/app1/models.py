from django.db import models

# Create your models here.
class Profile(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=100)
  city = models.CharField(max_length=70)
  state = models.CharField(max_length=150)





