from django.shortcuts import render, redirect
from .models import Todo
from .forms import todoForm

todos=Todo.objects.order_by('-date')[:8]

def show_todo(request,link_c):
    todo=Todo.objects.get(link_code=link_c)
    return render(request, "detail.html", {'todo': todo,'todos':todos})

def index(request):

    form=todoForm()
    if request.method=="POST":
        form=todoForm(request.POST)
        form.save()
        form=todoForm()
        
    
    return render(request, "index.html", {'form':form, 'todos':todos})


    
    
