from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Refferal
from clients.models import IntrestedClient
from django.contrib.auth.decorators import login_required
import uuid
#from users.serializers import UserSerializer
from users.models import User
#from django.contrib.auth.models import User
#from rest_framework.response import Response

# Create your views here.
def SalesRep(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        location = request.POST['location']
        phone = request.POST['phone']
        checked = request.POST['active']
        password = request.POST['password']
        code = uuid.uuid4().hex[:6].upper()

        sales_rep = Refferal(name=name, location=location, phone=phone, username=username, refferal_code=code, active=checked)
        sales_rep.save()
        messages.success(request, 'Thanks for joining our team ')

       
        
        user = User.objects.create_user(
            username= username,
            password=password,
            phone=phone,
        )

        return redirect('sales_dashboard')
    else:
        return render(request, 'sale_rep.html')
@login_required
def SalesDashboard(request):
    username= request.user.username
    try:
        sales_rep = Refferal.objects.get(username= username)
    except Refferal.DoesNotExist:
        sales_rep = None
    if sales_rep:
        refferal_code = sales_rep.refferal_code
        customers  = IntrestedClient.objects.filter(refferal_code=refferal_code)
    else:
        messages.error(request, 'You have to be one of our sales team to access the page!!!')
        return redirect('homepage')
    context = {'customers': customers, 'sales_rep': sales_rep}
    return render(request, 'sales_dashboard.html', context)