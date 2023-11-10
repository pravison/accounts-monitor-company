from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from refferals.forms import LoginForm

urlpatterns = [
    path('registeration/', views.registration, name='registration'),
    path('customer_invoice/<int:id>/', views.editInvoice, name='edit_invoice'),
    path('customer_invoice/', views.customerInvoice, name='customer_invoice'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name ='login'),
]