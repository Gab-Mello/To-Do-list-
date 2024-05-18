from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm, RegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.


def todo_list(request):
    tarefas = Todo.objects.all()
    return render(request,'ToDo/todo_list.html',{'tarefas': tarefas})

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()
    return render(request,'ToDo/todo_create.html',{'form': form})

@login_required
def todo_edit(request,pk):
    if request.method == 'POST':
        item = Todo.objects.get(pk=pk)
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        item = Todo.objects.get(pk=pk)
        form = TodoForm(instance=item)
        return render(request,'ToDo/todo_edit.html',{'form': form,'item': item})
    

@login_required
def todo_delete(request,pk):
    if request.method == 'POST':
        item = Todo.objects.get(pk=pk)
        item.delete()
        return redirect('home')
    else:
        item = Todo.objects.get(pk=pk)
        return render(request,'ToDo/todo_delete.html',{'item': item})  
    
@login_required
def todo_complete(requenst,pk):
    item = Todo.objects.get(pk=pk)
    item.completed()
    return redirect('home')

@login_required
def todo_delete_all(request):
    if request.method == 'POST':
        Todo.objects.all().delete()
        return redirect('home')
    else:
        return render(request,'ToDo/todo_delete_all.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        else:
            print('deu erro')
    else:
        form = RegistroForm()
    return render(request,'registration/registro.html',{'form': form})




