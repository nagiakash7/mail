import logging,requests
from django.shortcuts import render
from django.core.mail import get_connection,EmailMessage
from mail.settings import local as settings
from django.contrib import messages

# Create your views here.
def email_sending_func(request):
    if request.method == 'POST':
        try:
            # Sendgrid Email Sending Code
            email   = request.POST.get('email')
            connect = get_connection(host=settings.EMAIL_HOST,port=settings.EMAIL_PORT,username=settings.EMAIL_HOST_USER,password=settings.EMAIL_HOST_USER)
            sending = EmailMessage('Email Sent using Sendgrid Creds',body='Testing Sendgrid Email',from_email=settings.DEFAULT_FROM_EMAIL,to=[email],connection=connect)
            sending.content_subtype ='html'
            sending.send()
        except Exception as e:
            logging.error(e)
            try:
                # Mailgun Email Sending Code
                email = request.POST.get('email')
                response = requests.post("https://api.mailgun.net/v3/sandbox2affc1eb8d1c4b6b9104561f4e6daad6.mailgun.org/messages",auth = ("api", "ec49e59cec09a66c080326d28c52ed0d-c76388c3-a72d99e4"),
                    data = {
                      "from"    : "useremailmumbai@gmail.com",
                      "to"      : [f"{email}", "sandbox2affc1eb8d1c4b6b9104561f4e6daad6.mailgun.org"],
                      "subject" : "Email Send using Mailgun Creds",
                      "text"    : "Testing Mail Code Bravo !!!"})
                print(response)
                print('Email Send')
                messages.success('Email Send Successfully')
                return render(request, 'index.html')
            except Exception as e:
                logging.error(e)
    else:
        return render(request,'index.html')