from django.db import models
import datetime

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    age=models.IntegerField()
    batch=models.CharField(max_length=10,null=True)
    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False


    @staticmethod
    def get_user_by_email(email):
        try:
            return Customer.objects.get(email=email) # return one object only
        except:
            return False

    
    @staticmethod
    def get_by_id(c_id):
            return Customer.objects.filter(id=c_id) # return one object only


class Payment(models.Model):
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    payment_date=models.DateField(default=datetime.datetime.today)
    amount=models.IntegerField(default=500)


    def register(self):
        self.save()
     
    @staticmethod
    def get_payment_by_id(c_id):
            return Payment.objects.filter(id=c_id).order_by('-payment_date') # return one object only





    