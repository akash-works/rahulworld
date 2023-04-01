from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request,"index.html")

def blog(request):
    return render(request,"blog.html")

def about(request):
    return render(request,"about.html")


def contact(request):
        if  request. method =="POST":
                name = request .POST .get("name")
                email = request .POST .get("email")
                phone = request .POST .get("phone")
                message = request .POST .get ("message")
                a = Contact(name=name,email=email,phone=phone,message=message)
                a.save()
        return render(request,"contact.html")
        #     send_mail(
            
            
        #     email,
        #     name,
        #     message,
        #     phone,
        #     ['rahulwrold74@gmail.com'],
        #     fail_silently=False,
        #     )
        #     return  HttpResponse ( "msg sent" )
        # return render(request, 'contact.html')
#    if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             # Send email
#             send_mail(
#                 subject,
#                 'From: ' + name + '\n' + 'Email: ' + email + '\n\n' + message,
#                 email,
#                 ['admin@example.com'],
#                 fail_silently=False,
#             )

#             return render(request, 'success.html')
#     else:
#         form = ContactForm()

#     return render(request, 'contact.html', {'form': form})


def services(request):
    return render(request,"services.html")

def team(request):
    return render(request,"team.html")