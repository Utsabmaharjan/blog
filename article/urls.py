from django.urls import path
from article.views import List, Create_form, edit_form, delete_data, Blog_details

urlpatterns = [
    path('', List.as_view(), name= "Blog_page"),
    path('create', Create_form, name= "create_blog"),
    path('edit/<id>', edit_form, name= "edit_blog"),
    path('delete/<id>', delete_data, name= "delete_blog"),
    path('blog/<int:pk>', Blog_details.as_view(), name= "blog_detail"),

]