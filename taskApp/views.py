from django.shortcuts import render,redirect
from django.http import HttpResponse
from taskApp.models import Task
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        taskName = request.POST['taskName']
        if taskName == "":
            messages.warning(request, 'กรุณากรอกชื่องาน')
            return redirect('/')
        else:
            messages.success(request, 'บันทึกข้อมูลเรียบร้อย')
            newTask = Task.objects.create(name=taskName)
            newTask.save()
            return redirect('/')
    else:
        allTasks = Task.objects.all()
        context = {
            'allTasks': allTasks
        }
    return render(request, 'index.html',context)

def completed(request,task_id):
    task = Task.objects.get(pk=task_id)
    task.status = True
    task.save()
    return redirect('/')

def pending(request,task_id):
    task = Task.objects.get(pk=task_id)
    task.status = False
    task.save()
    return redirect('/')