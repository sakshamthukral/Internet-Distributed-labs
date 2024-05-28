from django.db import models

import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    city = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True, default="USA")
    def __str__(self):
        return self.name


class Book(models.Model):
    CATEGORY_CHOICES = [
        ('S', 'Scinece&Tech'),
        ('F', 'Fiction'),
        ('B', 'Biography'),
        ('T', 'Travel'),
        ('O', 'Other')
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='S')
    num_pages = models.PositiveIntegerField(default=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)
    description = models.TextField(default="No Description Available")
    def __str__(self):
        return self.title

class Member(User):
    STATUS_CHOICES = [
        (1, 'Regular member'),
        (2, 'Premium Member'),
        (3, 'Guest Member'),
    ]

    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=20, default="Windsor")
    province = models.CharField(max_length=2, default='ON')
    last_renewal = models.DateField(default=timezone.now)
    auto_renew = models.BooleanField(default=True)
    borrowed_books = models.ManyToManyField(Book, blank=True)
    address = models.CharField(max_length=300, blank=True, null=True)

class Order(models.Model):
    STATUS_CHOICES = [
        (0, 'Purchase'),
        (1, 'Borrow'),
    ]
    books = models.ManyToManyField(Book, blank=True)
    member = models.ForeignKey(Member, related_name='orders', on_delete=models.CASCADE)
    order_type = models.IntegerField(choices=STATUS_CHOICES, default=1)
    date = models.DateField(default=timezone.now)
