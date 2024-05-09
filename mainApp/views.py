from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def home(Request):
    return render(Request,"index.html")

def contact(Request):
    msg=''
    if(Request.method=="POST"):
        name=Request.POST.get('name')
        email=Request.POST.get('email')
        phone=Request.POST.get('phone')
        sub=Request.POST.get('subject')
        mess=Request.POST.get('message')
        msg='done'
        subject =sub
        message = f"""
    {mess}
    Client Details
    Name: {name}
    Email: {email}
    Phone: {phone}
    """
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["mithileshisdeveloper@gmail.com"]
        send_mail( subject, message, email_from, recipient_list )
        
    return render(Request,"contact.html",{'msg':msg})

def about(Request):
    return render(Request,"about.html")

def pictures(Request):
    return render(Request,"pictures.html")

def amenities(Request):
    return render(Request,"amenities.html")

def booknow(request):
    msg = ''
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        plot_num = request.POST.get('plot_num')
        plot_size = request.POST.get('plot_size')
        amount = request.POST.get('amount')
        aadhar = request.FILES.get('aadhar')
        msg = 'done'
        subject = "New Booking Received"
        message = f"""
        Client Details
        Name: {name}
        Email: {email}
        Phone: {phone}
        Plot Number: {plot_num}
        Plot Size: {plot_size}
        Amount: {amount}
        """
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["mithileshisdeveloper@gmail.com"]
        
        # Create an EmailMessage object
        email = EmailMessage(subject, message, email_from, recipient_list)
        
        # Attach the Aadhar file to the email
        if aadhar:
            email.attach(aadhar.name, aadhar.read(), aadhar.content_type)
        
        # Send the email
        email.send()

    return render(request, "booknow.html", {'msg': msg})
