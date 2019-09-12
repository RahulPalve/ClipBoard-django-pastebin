from django.shortcuts import render, redirect
from .models import Todo
from .forms import todoForm



def show_todo(request,link_c):
    todos=Todo.objects.order_by('-date')[:8]
    todo=Todo.objects.get(link_code=link_c)
    return render(request, "detail.html", {'todo': todo,'todos':todos})

def index(request):
    todos=Todo.objects.order_by('-date')[:8]
    todos=Todo.objects.all()
    form=todoForm()
    if request.method=="POST":
        form=todoForm(request.POST)
        form.save()
        form=todoForm()
    return render(request, "index.html", {'form':form, 'todos':todos})


    
