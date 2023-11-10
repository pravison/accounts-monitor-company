from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, Paginator
from . models import Blog, Tag, Categories, Comment
from homepage.models import  Company, Social_Links, Contact_us
from django.db.models import  Q
from django.contrib import messages

# Create your views here.
def blogView(request):
    infos = Company.objects.order_by('id')[:1]
    links = Social_Links.objects.all()
    contacts_infos = Contact_us.objects.order_by('id')[:1]
    blogs = Blog.objects.all().order_by('dateUpdated')
    paginator = Paginator(blogs, 5)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    posts = Blog.objects.order_by('-dateUpdated')[:5]
    tags = Tag.objects.all()
    categories = Categories.objects.all()


    # sort_by = request.GET.get('sort', 'l2h')
    # if sort_by == "l2h":
        # blogs = Blog.objects.order_by('-comments_count')
        # for blog in blogs:
        #     print(blog.comments_count)
    
                     
    context = {
        'blogs' :paged_blogs,
        'infos' : infos,
        'links' : links,
        'contacts_infos':contacts_infos,
        'posts' : posts,
        'tags' : tags,
        'categories' : categories
    }
    return render(request, 'blog.html', context)

def search(request):
    infos = Company.objects.order_by('id')[:1]
    links = Social_Links.objects.all()
    contacts_infos = Contact_us.objects.order_by('id')[:1]
    tags = Tag.objects.all()
    categories = Categories.objects.all()
    queryset_list = Blog.objects.order_by('-dateUpdated')
    category_id = request.GET.get('category', 0)
    tag_id = request.GET.get('tag', 0)
    query = request.GET.get('query')
    
    # paginator = Paginator(queryset_list, 2)
    # page = request.GET.get('page')
    # paged_blogs = paginator.get_page(page)
        # Keywords
    
    if query:
        queryset_list = queryset_list.filter(Q(content__icontains=query)| Q(title__icontains=query))
   
    if category_id :
        queryset_list = queryset_list.filter(categories__id=category_id )
    if tag_id :
        queryset_list = queryset_list.filter(tags__id=tag_id )
    
    context ={
        'infos' : infos,
        'links' : links,
        'contacts_infos':contacts_infos,
        'blogs': queryset_list,
        'tags' : tags,
        'categories' : categories,
        "category_id" : int(category_id)
    }
    return render(request, 'search.html', context)

def blogSingleView(request, id):
    blog = get_object_or_404(Blog, id=id)
    blogs = Blog.objects.filter(categories = blog.categories).exclude(id = blog.id)[:5]#reltaed blogs
    tags = Tag.objects.filter(blog__id = id)
    
    comments = blog.comment_set.all()
    context = {
        'blog': blog,
        'blogs' : blogs,
        'comments' : comments,
        'tags' : tags
    }
    return render(request, 'blog-single.html', context)


def comments(request):
    if request.method == 'POST':
        blog_id = request.POST['blog']
        blog = get_object_or_404(Blog, id=blog_id)
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['comment']

        comment = Comment(name=name, blog = blog, email=email, message=message)
        comment.save()
        messages.success(request, 'comment published successfuly!!')
        return redirect('http://www.localhost:8000/blog/' + blog_id  + '#comment' )