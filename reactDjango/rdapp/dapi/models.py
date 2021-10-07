from django.db import models



class Product(models.Model):
    width=600
    height=600
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='product/images' ,verbose_name='image' ,width_field='width',height_field='height')
    created_at =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title