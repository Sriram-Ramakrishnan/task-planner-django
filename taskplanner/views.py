from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .models import Task
from .forms import TaskForm
from django.utils import timezone


#-------------- Creating a user ------------------
def signupuser(request):
    data = {}
    if (request.method == 'GET'):
        # User is visiting the page
        return render(request, 'taskplanner/signupuser.html', data)
    else:
        # User clicks on submit => POST => Create User
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],request.POST['password1'])
                user.save()
                # Log them after signing up
                login(request,user)
                return redirect('home')
            except IntegrityError:
                data['error'] = "User already Exists. Choose a different username"
                return render(request, 'taskplanner/signupuser.html', data)

        else:
            data['error'] = "Passwords did not match"
            return render(request, 'taskplanner/signupuser.html', data)

#-------------- Main Page: Contains the tasks ------------------
def home(request):
    try:
        tasks = Task.objects.filter(user = request.user, completed_date__isnull=True)
        return render(request, 'taskplanner/home.html', {'tasks':tasks})
    except TypeError:
        return render(request, 'taskplanner/home.html')
#-------------- Logging out a user ------------------
def logoutuser(request):
    #Anything inside an url is a GET method
    # The urls loads automatically so if it is a GET method it will log them out
    if request.method == 'POST':
        logout(request)
        return redirect('home')

#-------------- Logging in a user ------------------
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'taskplanner/loginuser.html', {'form':AuthenticationForm()})
    else:
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        user = authenticate(username=username, password=password)
        x = None
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'taskplanner/loginuser.html', {'form':AuthenticationForm(), 'error': username })

#-------------- Add a task ------------------
def addtask(request):
    if request.method == 'GET':
        return render(request, 'taskplanner/addtask.html', {'form': TaskForm()})
    else:
        try:
            #----------Task created--------------
            form = TaskForm(request.POST)
            newtask = form.save(commit=False) # To not save in database immediately
            #Appending the task to the specific user 
            newtask.user = request.user
            newtask.save()
            return redirect('home')
        except ValueError:
            return render(request, 'taskplanner/addtask.html', {'form': TaskForm(),'error':'Improper data, try again!'})

#-------------- View a task separately -----------

def viewtask(request, task_pk):
    task = get_object_or_404(Task,pk=task_pk, user = request.user)
    data = {'task':task}
    if request.method == 'GET':
        form = TaskForm(instance=task)
        data['form'] = form
        return render(request, 'taskplanner/task.html', data)
    else:
        try:
            #----------Task Modified--------------
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('home')
        except ValueError:
            data['error'] = 'Improper data, try again!'
            data['form'] = form
            return render(request, 'taskplanner/task.html',data)

#----------------- Complete a task ------------------
def completetask(request,task_pk):
    task = get_object_or_404(Task,pk=task_pk, user = request.user)
    data = {'task':task}
    if request.method == 'POST':
        task.completed = True
        task.completed_date = timezone.now()
        task.save()
        return redirect('home')

#--------------- View Completed Tasks ---------------
def viewcompletedtasks(request):
    try:
        tasks = Task.objects.filter(user = request.user, completed_date__isnull=False).order_by('-completed_date')
        return render(request, 'taskplanner/completedtasks.html', {'tasks':tasks})
    except TypeError:
        return render(request, 'taskplanner/home.html')

#--------------- Delete a task ---------------
def deletetask(request, task_pk):
    task = get_object_or_404(Task,pk=task_pk, user = request.user)
    data = {'task':task}
    if request.method == 'POST':
        task.delete()
        return redirect('home')