from django.db import models

# Create your models here.


class Signup(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)




class Library_info(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    published = models.IntegerField()
    purchase = models.IntegerField(default=0)  # Fixed: Added parentheses
    price = models.IntegerField()
    quantity = models.IntegerField()
    sales = models.IntegerField()
