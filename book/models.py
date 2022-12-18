from django.db import models

# Create your models here.

class Category(models.Model):
    cat_title = models.CharField(max_length=50)
    cat_description = models.TextField()

    
    def __str__(self) -> str:
        return self.cat_title


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField(null=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    author = models.CharField( max_length=100)
    description = models.TextField()
    cover_image = models.ImageField( upload_to="books/",null=True , blank=True , height_field=None, width_field=None, max_length=None)


    def __str__(self) -> str:
        return self.title
