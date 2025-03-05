from django.db import models

# Create your models here.

class Pills(models.Model):
    maker = models.CharField(max_length=30)
    made_in = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    for_what = models.TextField(blank=True)
    use_instruction = models.TextField()
    made_date = models.DateField()
    expiration_date = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to='pill_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title}, {self.maker}, {self.created_at}"

    
