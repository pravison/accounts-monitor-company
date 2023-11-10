from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from clients.models import Newsletter, Contact_us_Message
from blog.models import Blog

# Create your views here.
def homepage(request):
    infos = Company.objects.order_by('id')[:1]
    contacts_infos = Contact_us.objects.order_by('id')[:1]
    links = Social_Links.objects.all()
    customers = Customer.objects.all()
    reviews = Testimonial.objects.all()
    teams = Team.objects.all()
    questions = Question.objects.all()
    features = Feature.objects.all()
    pricings = Pricing.objects.order_by('id')[:4]
    services = Service.objects.all()
    abouts = About_us.objects.order_by('id')[:1]
    blogs = Blog.objects.order_by('-dateUpdated')[:3]

    

    context = {
        'infos': infos,
        'contacts_infos': contacts_infos,
        'links':links,
        'customers': customers,
        'reviews': reviews,
        'teams': teams,
        'questions': questions,
        'pricings': pricings,
        'services': services,
        'features': features,
        'abouts' : abouts,
        'blogs' : blogs

    }
    return render(request, 'homepage.html', context)

def contactMessage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact_us_Message(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Thanks for reaching out, we will reply within two working days')
        return redirect('homepage')
def NewsLetter(request):
    if request.method == 'POST':
        email = request.POST['email']

        newsletter = Newsletter(email=email)
        newsletter.save()
        messages.success(request, 'thanks for subscribing to our newsletter!')
        return redirect('homepage')
   