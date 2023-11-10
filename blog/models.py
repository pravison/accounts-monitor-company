from django.db import models
#from tinymce.models import HTMLField

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    


class Blog(models.Model):
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    thumbnail = models.ImageField(blank=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    categories = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    comments_count = models.IntegerField(null=True, blank=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url
    @property
    def comment_count(self):
        try:
            comments_count = self.commnt_set.count()
        except:
            comments_count = 0
        return comments_count
    
class Comment(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(max_length=1000)
    blog = models.ForeignKey(Blog, blank=True, null=True, on_delete=models.SET_NULL) 
    date = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=True)
    replyId = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.name