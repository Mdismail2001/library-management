from django.db import models

# Create your models here.



from django.db import models

class Library_info(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    published = models.IntegerField()
    purchase = models.IntegerField(default=0)  # Fixed: Added parentheses
    price = models.IntegerField()
    quantity = models.IntegerField()
    sales = models.IntegerField()
