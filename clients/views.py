from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, InvoiceForm
from . models import IntrestedClient, Invoice
#from django_tenants.utils import schema_context
from users.models import User
from django.contrib.auth.decorators import login_required
from homepage.models import Company, Contact_us, Social_Links

# Create your views here

def registration(request):
    infos = Company.objects.order_by('id')[:1]
    contacts_infos = Contact_us.objects.order_by('id')[:1]
    links = Social_Links.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            name = form.cleaned_data['name']
            business_name = form.cleaned_data['business_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            location = form.cleaned_data['location']
            refferal_code = form.cleaned_data['refferal_code']
            password = form.cleaned_data['password']

            #create tenant
            new_tenant = IntrestedClient(name=name, username=username, business_name=business_name, refferal_code=refferal_code, email=email, phone=phone, location=location)
            new_tenant.save()
            messages.success(request, 'Thanks for taking a step to join us, we look forward working with you!!!')
            #register user
            user = User.objects.create_user(
                        username= username,
                        password=password,
                        phone=phone,
                    )
            #create invoice
            Invoice.objects.create(
                customer = new_tenant
            )

            return redirect('customer_invoice')
            #return redirect('https://frontendaccountsmonitor.vercel.app/')
    else:
        form = RegistrationForm()
    context = {
        'form':form,
        'infos': infos,
        'contacts_infos': contacts_infos,
        'links' :links

    }
    return render(request, 'register.html', context)

@login_required
def customerInvoice(request):
    username= request.user.username
    try:
        customer = IntrestedClient.objects.get(username= username)
    except IntrestedClient.DoesNotExist:
        customer = None
    if customer:
        invoices  = Invoice.objects.filter(customer=customer)
        context = {'invoices': invoices, 'username':username, 'customer': customer}
        return render(request, 'customer_invoice.html', context)
    else:
        messages.error(request, 'You have to register first as our customer to access the page!!!')
        return redirect('homepage')
    

@login_required
def editInvoice(request, id):
    if request.method == 'POST':
        invoice= Invoice.objects.get(id=id)
        form = InvoiceForm(request.POST, instance=invoice)

        if form.is_valid():
            form.save
            context= {
                'form': form,
                'invoice': invoice,
                }
            return render(request, 'edit_profile.html', context)
    else:
        invoice= Invoice.objects.get(id=id)
        form = InvoiceForm(instance=invoice)

    context= {
                'form': form,
                'invoice': invoice
            }



























































































































































            
    return render(request, 'edit_invoice.html', context)
 