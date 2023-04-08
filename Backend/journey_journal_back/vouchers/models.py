from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Voucher(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=300)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    hire_date = models.DateField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
