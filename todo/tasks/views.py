from django.shortcuts import render, redirect, reverse
from .models import Task
from .forms import TaskForm

# Create your views here.


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('index'))

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    context = {'form': form}

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect(reverse('index'))

    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    context = {'task': task}

    if request.method == 'POST':
        task.delete()

        return redirect(reverse('index'))

    return render(request, 'tasks/delete.html', context)
