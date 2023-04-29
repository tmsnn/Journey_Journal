from django.db import models
from django.contrib.auth.hashers import check_password


class Category(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Voucher(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.CharField(max_length=300, default='')
    img = models.CharField(max_length=300, default='')
    like = models.IntegerField(default=0)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    img = models.CharField(max_length=300, default='')

    def __str__(self):
        return f"{self.id} - {self.name}"



class Comment(models.Model):
    username = models.CharField(max_length=300, default='Anonymous')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    def __str__(self):
            return f"{self.id} - {self.voucher}"


