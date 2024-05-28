from django.contrib import admin

# Register your models here.
from .models import Publisher, Book, Member, Order

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Order)
