from django.shortcuts import render
from .forms import Field,Login
from .models import User, Transactions

# Create your views here.

def index(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    if 'Windows' in user_agent or 'Mac' in user_agent:
        form = Login()
        return render(request, 'login.html', {'field':form})
        #return render(request,'pc.html')
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

                history_send = Transactions.objects.filter(send=userdata) if Transactions.objects.filter(send=userdata) else None
                history_rec = Transactions.objects.filter(rec=userdata) if Transactions.objects.filter(rec=userdata) else None 
                return render(request, 'dashboard.html',{'user':userdata,'history_send':history_send,'history_rec':history_rec,"field":field})
            else:
                return render(request,'error.html',{'code':404,'desc':'No User Found'})
        else:
            error(request,"Bad Request",400)
    else:
        error(request,"Internal Server Error",500)

def error(request, desc, code):
    return render(request,'error.html',{'code':code,'desc':desc})

def pay(request, send):
    if request.method == "POST":
        form = Field(request.POST)
        if form.is_valid():
            rec = form.cleaned_data['tag']
            cvv = form.cleaned_data['cvv']
            return render(request,'pc.html')
        else:
            print('error')