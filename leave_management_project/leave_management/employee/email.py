from django.core.mail import send_mail


def send_welcome_mail(recepients,message,**kwargs):
    if isinstance(recepients,str):
        recepients=[recepients]
    send_mail("thankyou for register", message=message, from_email="sanket619sathone@gmail.com",
              recipient_list=recepients,fail_silently=True)
    
def send_leave_mail(recepients, message, **kwargs):
    if isinstance(recepients, str):
        recepients=[recepients]
    send_mail(f"leave applied by {recepients}",message=message, from_email="sanket619sathone@gmail.com",recipient_list=recepients, fail_silently=True)


