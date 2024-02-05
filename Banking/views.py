from django.shortcuts import render, redirect
from .forms import Login
from .models import User, Transactions
from django.db.models import Q

# Create your views here.

def index(request):
    form = Login()
    return render(request, 'login.html', {'login':form})

def dash(request):
    if request.method=='POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            try:
                userdata = User.objects.get(accountno=username,password=passwd)
                history_send = Transactions.objects.filter(send=userdata)
                history_rec = Transactions.objects.filter(rec=userdata)
                return render(request, 'dashboard.html',{'adminlist':['President','CIO','CEO','MD'],'post':userdata.post,'user':userdata,'history_send':history_send,'history_rec':history_rec})
            except:
                return render(request,'error.html',{'code':404,'desc':'No User Found'})
        else:
            error(request,"Bad Request",400)
    else:
        error(request,"Internal Server Error",500)

def error(request, desc, code):
    return render(request,'error.html',{'code':code,'desc':desc})