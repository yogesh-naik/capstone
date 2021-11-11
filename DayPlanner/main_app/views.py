from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from .forms import TaskForm,TaskEditForm
from main_app.models import Task

# Create your views here.
@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"

@login_required
def About(request):
    # template_name = "about.html"
    return render(request,"about.html")


@login_required
def CreateTask(request):
    form = TaskForm()
    context = {}
    if request.method == 'POST':
        form = TaskForm(request.POST)
        # form['user'] = request.user
        if form.is_valid():
            form.save()
            return redirect('/addtask')
    
    context["tasks"] = Task.objects.filter(user=request.user)
    context["header"] = "Trending Artists"
    # print(context)
    context['form']=form
    # print(context)
    return render(request, 'create_task.html', context)


@login_required
def UpdateTask(request,pk):
    singletask = Task.objects.get(id=pk)
    form = TaskEditForm()
    if request.method == 'POST':
        form = TaskEditForm(request.POST,instance =singletask)
        # form['user'] = request.user
        if form.is_valid():
            form.save()
            return redirect('addtask')
    
    context = {'form':form}
    context['task'] = singletask
    return render(request,"update_task.html",context) 


@login_required
def DeleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
    return redirect('/addtask')
    
    # return render(request,"artist_delete.html") 