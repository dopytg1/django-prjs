from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.http import HttpResponseRedirect, HttpResponseNotFound


def main(request):
    tasks = Task.objects.all()

    return render(request, 'main/index.html', {'title': "Цели", 'tasks': tasks})

def about_us(request):
    return render(request, 'main/about-us.html')

def create_goal(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Something wrong"
    else:
        form = TaskForm()

    return render(request, 'main/create.html', {'form': form, 'error': error})


def delete_goal(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def change_goal(request, id):
    try:
        task = Task.objects.get(id = id)

        if request.method == 'POST':
            task.title = request.POST.get('title')
            task.task = request.POST.get('goal')
            task.save()

            return HttpResponseRedirect("/")
        else:
            return render(request, "main/change.html", {"task": task})
    
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Goal not found</h2>")