from django import forms
from article.models import Blog

class CreateForm (forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        

class EditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        
        