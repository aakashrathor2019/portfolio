from django.shortcuts import render,redirect
from .models import Contact
import re

# Create your views here.
def home(request):
	context={'home':'active'}
	return render(request,'core/home.html',context)

def contact(request):
	context={'contact':'active'}
	return render(request,'core/contact.html',context)

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

