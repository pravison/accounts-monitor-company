from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . forms import LoginForm
urlpatterns = [
    path('', views.SalesRep, name='sales_rep'),
    path('sales_dashboard/', views.SalesDashboard, name='sales_dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name ='login'),
]