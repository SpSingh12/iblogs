from django.shortcuts import render
from blog.models import Category, Post,Contacts
from django.contrib import messages
from django.core.mail import send_mail

from django.conf import settings


# Create your views here.
def blog(request):
    posts=Post.objects.all()[:11]
    # print(post)

    # cats = Category.objects.all()
    data = {
        'posts':posts,
        # 'cats':cats
    }
    return render(request,'blog.html',data)


def home(request):
    # load aall the post from db
    posts=Post.objects.all()[:11]
    # print(post)

    cats = Category.objects.all()
    data = {
        'posts':posts,
        'cats':cats
    }
    return render(request,'home.html',data)


def post(request, url):
    post=Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request,'posts.html',{'post':post,'cats':cats})



def category(request, url):
    cat = Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,'category.html',{'cat':cat,'posts':posts})


def contact(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        describe=request.POST['describe']
        send_mail(
            '@suryapratapsingh',
            'YOUR FORM HAVE BEEN SUBMITTED SUCCESSFULLY',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        if len(name) < 2  or len(email) < 10 or len(phone) < 10 or len(describe) < 10:
            messages.error(request,'PLEASE FILL FORM CORRECTLY')
        else:
            contact=Contacts(name=name,phone=phone,email=email,describe=describe)
            contact.save()
            messages.success(request, 'YOUR FORM HAVE BEEN SUBMITTED PLEASE CHECK YOUR EMAIL')
    return render(request,'contact.html')



def about(request):
    return render(request,'about.html')