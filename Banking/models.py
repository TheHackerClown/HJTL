from django.db import models

# Create your models here.

class User(models.Model):
    rfid = models.BigAutoField(primary_key=True)
    tag = models.CharField(max_length=10,default='hehe')
    name = models.CharField(max_length=50)
    accountno = models.IntegerField()
    cvv = models.IntegerField()
    balance = models.IntegerField()
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.name} {self.rfid}"

class Transactions(models.Model):
    rfid = models.BigAutoField(primary_key=True)
    send = models.ForeignKey(User, on_delete=models.CASCADE, related_name='send')
    rec = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rec')
    date = models.DateTimeField(auto_now=True)
    balance= models.IntegerField(default=0)
    status = models.CharField(max_length=20,default='Processing')
    

    def __str__(self):
        return f"{self.rfid}: {self.send} --> {self.rec} on {self.date} "