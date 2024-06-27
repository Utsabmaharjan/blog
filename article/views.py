from django.shortcuts import render, redirect
from article.models import Blog
from article.form import CreateForm, EditForm
from django.views.generic import ListView, DetailView



# Create your views here.

def Create_form(request):
       form = CreateForm
       if request.method=='POST':
               form= CreateForm(request.POST, request.FILES)
               if form.is_valid():
                       form.save()
                       return redirect('/')
               else:
                       print(form.errors)
       context = {
        "form": form
        } 
       return render(request, 'create.html', context)          

def edit_form(request, id):
    eblog = Blog.objects.get(id=id)
    form = EditForm (instance=eblog) 
    if request.method=='POST':
        form = EditForm(request.POST ,request.FILES or None, instance=eblog)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)

    context ={
        "data":eblog,
        "form":form
    }
    return render(request,'edit.html', context)


def delete_data(request, id):
    blog = Blog.objects.get(id=id).delete()
    return redirect ('/')
   

class List(ListView):
      model = Blog
      template_name = 'index.html'
      context_object_name = 'data'
    
class Blog_details(DetailView):
    model= Blog
    template_name = 'data.html'
    context_object_name = 'data'