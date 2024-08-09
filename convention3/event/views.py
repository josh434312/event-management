from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.utils.crypto import get_random_string
from django.contrib import messages 
from .models import Ticket

# Create your views here.

def index(request):   
    return render(request, 'event/index.html', {}) 

def about(request):   
    return render(request, 'event/about.html', {}) 

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
                messages.info(request, 'Username Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:

            
                User.objects.create_user(username=username,email=email,
                password=password1,first_name=first_name)
        else:
            messages.info(request,'password not matching....')
            return redirect('register')

        return redirect ('login_user')
    return render(request, 'event/register.html', {})
 

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
              
            if not hasattr(user,'ticket'):
                ticket_number = get_random_string(length=10)
                Ticket.objects.create(user=user,ticket_number=ticket_number)
            
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login_user')
        return redirect('/')
    return render(request, 'event/login_user.html',{})

def logout_user(request):
    logout(request)
    return redirect('/')

def speakers(request):
    return render(request, 'event/speakers.html',{})


def dashboard(request):
    ticket = request.user.ticket
    return render(request, 'event/dashboard.html',{'ticket':ticket})

def tickets(request):
    return render(request, 'event/tickets.html',{})


def ticket_details(request):
    return render(request, 'event/ticket_details.html',{})



def rent_venue(request):
    return render(request, 'event/rent_venue.html',{})



def shows_events(request):
    return render(request, 'event/shows_events.html',{})
