from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogUpdate
from django.core.paginator import Paginator
from faker import Faker
from django.contrib.auth.models import User

# Create your views here.
def hello(request):
    return render(request, 'hello.html')

def blog(request):
    blogs = Blog.objects #가지고오기

    blog_list = Blog.objects.all() #쿼리셋으로 가지고오기. 쿼리셋은 DB에 접근하기 쉽도록 쓰는 언어?
    paginator = Paginator(blog_list, 5) #가지고 온 것 page단위로 뿌리기 

    page = request.GET.get('page') #페이지에 들어갈 내용 가지고 와줘

    articles = paginator.get_page(page) # 내용을 뿌린다.
    return render(request, 'blog.html', {'blogs' : blogs, 'articles' : articles}) # html에 뿌릴수 있는 객체들을 보낸다.

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id) 
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    if request.user.is_authenticated:
        blog.writer = request.user.get_username()
    else:
        blog.writer = ""
    blog.save()
    return redirect("/blog/" + str(blog.id))

def delete(request, blog_id):
    Blog.objects.get(id = blog_id).delete()
    return redirect('/')


def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('/blog/' + str(blog.id))
    else:
        form = BlogUpdate(instance = blog)
 
        return render(request,'update.html', {'form':form})

def introduce(request):
    return render(request, 'introduce.html')

def fake(request):
    for i in range(10):
        blog = Blog()
        fake = Faker()
        blog.title = fake.name()
        blog.body = fake.sentence()
        blog.pub_date = timezone.datetime.now()
        blog.save()
        
    return redirect('/')


