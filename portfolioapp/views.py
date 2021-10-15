from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import message, send_mail,BadHeaderError
from .models import About,Project,Skills,Tag
# Create your views here.


def index(request):
    
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        message='''
        I'm{} \n {}\n my email ( {} )
        '''.format(name,message,email)
        try:
            send_mail(subject,message,email,['abdullahelsaayed@gmail.com','abdullahelsaayed@outlook.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        return HttpResponse('<h1> Success! Thank you for your message.</h1>')



    
    skills=Skills.objects.all()   
    categorys=Tag.objects.all()
    about=About.objects.last()
    projects=Project.objects.all()
    context={'about':about,'categorys':categorys,'skills':skills,'projects':projects}
    # return HttpResponse('fsdfsdfs')
    return render(request,'portfoiloapp/index.html',context)