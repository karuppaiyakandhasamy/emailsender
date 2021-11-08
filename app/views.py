from django.shortcuts import render
from django.core.mail import send_mail
from .forms import contform
# Create your views here.
def index(request):
    if request.method == "GET":
        form = contform()
    else:
        form = contform(request.POST)
        if form.is_valid():
            email =form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            send_mail(subject,message,email,['karuppaiyakandhasamy1@gmail.com',email])
    return render(request,'app/send.html',{'form':form})
