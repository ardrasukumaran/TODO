from django.shortcuts import render, redirect
#Create a new list
from .models import ToDoList
# Create your views here.
def index(request):
    if request.POST:
        new_task=request.POST['task'].strip()
        todolist=ToDoList(task_title=new_task)
        todolist.save()
        return redirect('index')
    

    todolist=ToDoList.objects.all()
    return render(request,'todolist/index.html',context={'tasks':todolist})

def deleteTask(request,id):
    task = ToDoList.objects.get(taskid=id)
    task.delete()
    return redirect('index')

def editTask(request,id):
    task = ToDoList.objects.get(taskid=id)

    if request.POST:
        new_task = request.POST['task'].strip()
        new_desc = request.POST['description']
        task.task_title = new_task
        task.task_description = new_desc
        task.save()
        return redirect('index')
    
    return render(request,'todolist/edit.html',context={'task':task})


