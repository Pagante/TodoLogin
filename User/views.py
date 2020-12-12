from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import TodoListForm
from django.views.decorators.http import require_POST

from .models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    context={}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    context['form'] = form

    return render(request, 'registration/signup.html', context)

@login_required()
def TodoAppList(request):
    todo_items = User.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_items':todo_items, 'form':form}
    return render(request, 'todoList.html', context)

@require_POST
def addTodoList(request):
    form = TodoListForm(request.POST)

    if form.is_valid():
        new_todo = User(text=request.POST['text'])
        new_todo.save()
    return redirect("TodoAppList")


def completeTodo(request, user_id):
    todo = User.objects.get(pk =user_id)
    todo.completed =True
    todo.save_base()

    return redirect('TodoAppList')

def deleteCompleted(request):
    todo = User.objects.filter(completed__exact=True).delete()

    return redirect('TodoAppList')

def deleteAll(request):
    User.objects.all().delete()

    return redirect('TodoAppList')
