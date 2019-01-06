from django.shortcuts import render, HttpResponse
from .models import Todo
from .forms import todoForm


def index(request):
    todos=Todo.objects.all()
    form=todoForm()
    if request.method=="POST":
        form=todoForm(request.POST)
        form.save()
        form=todoForm()
    
    return render(request, "index.html", {'form':form, 'todos':todos})

def show_todo(request,td_no):
    todos=Todo.objects.all()
    for todo in todos:
        if todo.link_code==td_no:
            ptd=todo
    return render(request, "detail.html",{'td_no':td_no,'ptd':ptd})
    
    
