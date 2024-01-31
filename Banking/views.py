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
            userdata = User.objects.get(accountno=username,password=passwd)
            if userdata:
                print(userdata.accountno)
                history_send = Transactions.objects.filter(send=userdata)
                history_rec = Transactions.objects.filter(rec=userdata)
                if history_rec or history_send:
                    return render(request, 'dashboard.html',{'user':userdata,'history_send':history_send,'history_rec':history_rec})
                else:
                    index(request)
            else:
                index(request)
    else:
        index(request)
