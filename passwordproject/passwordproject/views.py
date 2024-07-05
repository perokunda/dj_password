from django.core.mail import send_mail
from django.http import HttpResponse

def emailfunc(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'opapi@gogolinux.net',
        ['opapi@gogolinux.net'],
        fail_silently=False,
    )
    return HttpResponse('')
    
    