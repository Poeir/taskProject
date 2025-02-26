from django.shortcuts import render,redirect
from django.http import HttpResponse
from taskApp.models import Task
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method == 'POST':
        taskName = request.POST['taskName']
        if taskName == "":
            messages.warning(request, 'กรุณากรอกชื่องาน')
            return redirect('/')
        else:
            messages.success(request, 'บันทึกข้อมูลเรียบร้อย')
            newTask = Task.objects.create(name=taskName,manager = request.user)
            newTask.save()
            return redirect('/')
    else:
        allTasks = Task.objects.filter(manager = request.user)
         # Pagination
        page = request.GET.get('page')
        paginator = Paginator(allTasks, 5)
        allTasks = paginator.get_page(page)
        context = {
            'allTasks': allTasks
        }
    
    return render(request, 'index.html',context)

@login_required(login_url='/login')
def completed(request,task_id):
    task = Task.objects.get(pk=task_id)
    if task.manager == request.user:
        task.status = True
        task.save()
        return redirect('/')
    else:
        messages.warning(request, 'คุณไม่มีสิทธิ์แก้ไขงานนี้')
        return redirect('/')
@login_required(login_url='/login')
def pending(request,task_id):
    task = Task.objects.get(pk=task_id)
    if task.manager == request.user:
        task.status = False
        task.save()
        return redirect('/')
    else: 
        messages.warning(request, 'คุณไม่มีสิทธิ์แก้ไขงานนี้')
    return redirect('/')