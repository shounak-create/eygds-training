from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField(default=0)
    contact = models.CharField(max_length=15, default="0000000000")

    def __str__(self):
        return self.name
