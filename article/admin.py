from django.contrib import admin
from article.models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['id','title','details','created_at']
    search_fields=['id','title']
