from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import taskForm
# Create your views here.
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

def home(request):
    return render(request, 'taskplanner/home.html')

def logoutuser(request):
    #Anything inside an url is a GET method
    # The urls loads automatically so if it is a GET method it will log them out
    if request.method == 'POST':
        logout(request)
        return redirect('home')

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


def addtask(request):
    if request.method == 'GET':
        return render(request, 'taskplanner/addtask.html', {'form': taskForm()})
    else:
        try:
            #----------Task created--------------
            form = taskForm(request.POST)
            newtask = form.save(commit=False) # To not save in database immediately
            #Appending the task to the specific user 
            newtask.user = request.user
            newtask.save()
            return redirect('home')
        except ValueError:
            return render(request, 'taskplanner/addtask.html', {'form': taskForm(),'error':'Improper data, try again!'})

