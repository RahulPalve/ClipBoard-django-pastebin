from django.shortcuts import render, redirect
from .models import Todo
from .forms import todoForm



def show_todo(request,link_c):
    todos=Todo.objects.order_by('-date')[:8]
    todo=Todo.objects.get(link_code=link_c)
    return render(request, "detail.html", {'todo': todo,'todos':todos})

def all(request):
    todos = Todo.objects.all()
    return render(request, 'all.html', {'todos': todos})

def index(request):
    todos=Todo.objects.order_by('-date')[:8]
    todos=Todo.objects.all()[:8]
    form=todoForm()
    if request.method=="POST":
        form=todoForm(request.POST)
        form.save()
        form=todoForm()
    return render(request, "index.html", {'form':form, 'todos':todos})


    
