from django.shortcuts import render
from .forms import Field,Login
from .models import User, Transactions

# Create your views here.

def index(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    if 'Windows' in user_agent or 'Mac' in user_agent:
        return render(request,'pc.html')
    else:
        form = Login()
        return render(request, 'login.html', {'field':form})

def dash(request):
    if request.method=='POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            field = Field()
            userdata = User.objects.get(accountno=username,password=passwd)
            if userdata:

                history_send = list(reversed(Transactions.objects.filter(send=userdata))) if Transactions.objects.filter(send=userdata) else None
                history_rec = list(reversed(Transactions.objects.filter(rec=userdata))) if Transactions.objects.filter(rec=userdata) else None 
                return render(request, 'dashboard.html',{'user':userdata,'history_send':history_send,'history_rec':history_rec,"field":field,'tag':userdata.tag})
            else:
                return render(request,'error.html',{'code':404,'desc':'No User Found'})
        else:
            return render(request,'error.html',{'code':404,'desc':'Site Kharab hogyi'})
    else:
        return render(request,'error.html',{'code':404,'desc':'Site Kharab hogyi'})

def error(request, desc, code):
    return render(request,'error.html',{'code':code,'desc':desc})

def pay(request):
    if request.method == "POST":
        form = Field(request.POST)
        if form.is_valid():
            rec = form.cleaned_data['tag']
            cvv = form.cleaned_data['cvv']
            amt = form.cleaned_data['amt']
            sender = User.objects.get(cvv=cvv)
            if sender:
                reciever = User.objects.get(tag=rec)
                if reciever:
                    sender.balance -= amt
                    reciever.balance += amt
                    reciever.save()
                    sender.save()
                    Transactions.objects.create(send=sender,rec=reciever,balance=amt)
                    return render(request,'redirect.html')
                else:
                    return render(request,'error.html',{'code':404,'desc':'Site Kharab hogyi'})
            else:
                return render(request,'error.html',{'code':404,'desc':'Site Kharab hogyi'})
        else:
            return render(request,'error.html',{'code':404,'desc':'Site Kharab hogyi'})