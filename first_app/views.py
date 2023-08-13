from django.shortcuts import render,redirect
from first_app.forms import TaskForm
from first_app.models import TaskModel
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request,'home.html')

class TaskFormView(CreateView):
    model = TaskModel
    template_name = 'add_tasks.html'
    form_class = TaskForm
    success_url = reverse_lazy('show_tasks')


def show_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=False)
    return render(request, 'show_tasks.html', {'data': tasks})


class EditTaskView(UpdateView):
    model = TaskModel
    template_name = 'add_tasks.html'
    form_class = TaskForm
    success_url = reverse_lazy('show_tasks')

class DeleteTaskView(DeleteView):
    model = TaskModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('show_tasks')

    
def complete_task(request, pk):
    task = TaskModel.objects.get(id=pk)
    task.is_completed = True
    task.save()
    return redirect('completed_tasks')

def completed_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'completed_tasks.html', {'data': tasks})