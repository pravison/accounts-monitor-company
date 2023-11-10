from django.db import models
#from tinymce.models import HTMLField

# Create your models here.
class Company(models.Model):
    hero_image = models.ImageField(blank=True)
    name = models.CharField(max_length=150)
    pitch = models.TextField(max_length=250)
    tagline = models.TextField(max_length=150)

    class Meta:
        verbose_name_plural = 'Company'
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.hero_image.url
        except:
            url = ''
        return url

class About_us(models.Model):
    image = models.ImageField(blank=True)
    hook = models.TextField(max_length=300)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.hook
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Feature(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    icon = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Question(models.Model):
    question = models.TextField(max_length=300)
    answer = models.TextField(max_length=300)

    def __str__(self):
        return self.question
    
class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    message = models.TextField(max_length=1000)
    job_position = models.CharField(max_length=150)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url

class Team(models.Model):
    name = models.CharField(max_length=150)
    photo =  models.ImageField(blank=True)
    job_position =  models.CharField(max_length=150)
    overview =  models.TextField(max_length=400)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url

class Customer(models.Model):
    logo = models.ImageField(blank=True)
    name = models.CharField(max_length=150)

    @property
    def imageURL(self):
        try:
            url = self.logo.url
        except:
            url = ''
        return url
    

    def __str__(self):
        return self.name
    
   
class Pricing(models.Model):
    plan = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    color = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    feature = models.ManyToManyField(Feature, blank=True)

    def __str__(self):
        return self.plan
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

class Contact_us(models.Model):
    phone1 = models.CharField(max_length=16)
    phone2 = models.CharField(max_length=16)
    email1 = models.EmailField()
    email2 = models.EmailField()
    address = models.CharField(max_length=100)
    location =models.CharField(max_length=100)
    county = models.CharField(max_length=16)
    country = models.CharField(max_length=16)

    def __str__(self):
        return self.phone1

class Social_Links(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name




