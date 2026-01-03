from django.db import models

# Create your models here.
class Property(models.Model):
    photo = models.ImageField(upload_to='images')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=300)
    listed_date = models.DateTimeField(auto_now_add=True)
    # For tracking updates
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title       