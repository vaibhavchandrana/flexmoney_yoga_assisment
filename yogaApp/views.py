from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from yogaApp.models import Customer,Payment
from django.contrib.auth.hashers import make_password, check_password
import datetime


def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password = request.POST.get('pass')
        c_pass = request.POST.get('c_pass')
        phone = request.POST.get('phone')
        batch = request.POST.get('batch')
        print(name, email, age, password, c_pass, phone, batch)
        customer = Customer(name=name, email=email, phone=phone,
                            password=password, age=age, batch=batch)
        customer.password = make_password(customer.password)
        isExist = customer.isExists()
    
        if isExist:
            error = "Email already registered"
            return render(request, 'index.html', {'error': error})
       
        customer.register()
        
        request.session['customer_id'] = customer.id
        request.session['customer_email'] = customer.email
        cid=request.session.get('customer_id')
        makePayment=Payment(customer_id=Customer(id=cid))
        makePayment.register()
        return redirect('profile')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('pass')
        customer = Customer.get_user_by_email(
            email)  # return object matching email
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                return redirect('profile')
            else:
                error = "Invalid email or password !!! "
                return render(request, 'login.html', {'error': error})

        else:
            error = "Invalid email or password !!! "
            return render(request, 'login.html', {'error': error})



def Profile(request):
    if request.session.get('customer_id'):
        cid=request.session.get('customer_id')
        email=request.session.get('customer_email')
        user=Customer.get_user_by_email(email=email)
        print(user.id)
        pay=Payment.get_payment_by_id(user.id)
        if pay:
            print(pay)
            transaction=pay[0].payment_date
            today = datetime.datetime.now()
            month = today.month
            transMonth=transaction.month
            flag=False
            if month==transMonth:
                flag=True
        else:
            flag=False

        return render(request,'profile.html',{"users":user,"flag":flag})
    else:
        return redirect('login')

def complete_payment(request):
    if request.session.get('customer_id'):
        cid=request.session.get('customer_id')
        makePayment=Payment(customer_id=Customer(id=cid))
        makePayment.register()
        
        return redirect('profile')
    else:
        return redirect('login')

def ChangeBatch(request):
    if request.method=="POST" and request.session.get('customer_id'):
        newbatch = request.POST.get('batch')
        cid=request.session.get('customer_id')
        customer=Customer.get_by_id(cid)
        customer.update(batch=newbatch)
        return redirect('profile')
    else:
        return redirect('login')


