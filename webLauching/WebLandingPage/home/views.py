from django.contrib import messages
from django.shortcuts import render
from .forms import *
# Create your views here.

def index(request):
    if request.method == "POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            f=Contact(
                name=request.POST['name'],
                email=request.POST['email'],
                message=request.POST['message'],
            )
            f.save()
            messages.success(request, f"You sent!!!")
    else:
        form=ContactForm
    context={'form':form}
    return render(request,'home/index.html',context)