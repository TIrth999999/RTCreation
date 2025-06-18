from django.db import models

class VisitorCounter(models.Model):
    count = models.IntegerField(default=0)

class Reviews(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    desc = models.TextField()
    rating = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField(null=True)
    desc = models.TextField(null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name