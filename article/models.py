from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(verbose_name='Blog title', max_length= 40)
    image = models.ImageField(upload_to='blog-img/')
    details = models.TextField(verbose_name='Details')
    created_at = models.DateField(auto_now_add= True)
    
    def __str__(self):
        return self.title
