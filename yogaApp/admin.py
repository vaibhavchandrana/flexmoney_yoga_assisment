from django.contrib import admin
from yogaApp.models import Customer,Payment


class AdminCustomer(admin.ModelAdmin):
    list_display=['name','email','phone','password','age','batch']

class AdminuserPayment(admin.ModelAdmin):
    list_display=['customer_id','payment_date','amount']



# Register your models here.
admin.site.register(Customer,AdminCustomer)
admin.site.register(Payment,AdminuserPayment)
