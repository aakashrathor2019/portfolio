from django.shortcuts import render,redirect
from .models import Contact
import re
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def home(request):
	context = {'home': 'active'}
	return render(request, 'core/home.html', context)


def contact(request):
	context = {'contact': 'active'}
	return render(request, 'core/contact.html', context)


def contact_form_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print('Name, Email, Subject, Message is-->>', name, email, subject, message)

        # Validate the input data
        if name and email and subject and message:
            # Check if the name contains numbers
            if any(char.isdigit() for char in name):
                return render(request, 'core/contact.html', {'error': 'Name cannot contain numbers.'})
            
            # Validate email format
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|in)$'
            if not re.match(email_regex, email):
                return render(request, 'core/contact.html', {'error': 'Invalid email format. Please enter a valid email.'})

            # Save data to the database
            data = Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            print('Data is:', data)
            data.save()
            return redirect("home")
        else:
            return render(request, 'core/contact.html', {'error': 'All fields are required.'})

    context = {'contact': 'active'}
    return render(request, 'core/contact.html', context)

def login_view(request):
    if request.method == "POST":
        print('inside login fun')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'core/login.html', {'error':'Enter Valid username or password'})
    return render(request, 'core/login.html')


@login_required(login_url='login')
def dashboard(request):
    user_messages = Contact.objects.all().order_by('-id')
    return render(request, 'core/dashboard.html', {'data': user_messages})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def detail_view(request, id):
    data = Contact.objects.get(id=id)
    return render(request, 'core/detail_view.html', {'data': data})
