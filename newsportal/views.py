from django.shortcuts import render,HttpResponse,redirect
from blog.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def about(request):
    return render(request,'about.html')

def views_more(request,id):
    data = Blog.objects.get(pk=id)
    context = {
        'Blog' : data
    }
    return render(request,"views_more.html",context)

def home(request):
    data = Blog.objects.all()
    context = {
        'Blog' : data
    }

    return render(request,'home.html',context)

def signin(request):
    if (request.method=='GET'):
        return render(request,'login.html')
    else:
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        if user is not None:
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "passsword match vayena")
            return redirect('signin')

def signup(request):
    if (request.method=='GET'):
        return render(request,'signup.html')
    else:
        u = request.POST['username']
        e = request.POST['email']
        p1 = request.POST['password']
        p2 = request.POST["cpassword"]

        if (p1==p2):
            u = User(username=u,email=e)
            u.set_password(p1)
            u.save()
            messages.add_message(request, messages.SUCCESS, "sign up succcess")
            return redirect('signin')
        else:
           
            messages.add_message(request, messages.ERROR, "babu password match huney gari hana na")
            return redirect('signup')

def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def dashboard(request):
    return render(request,'dashboard.html')

def create_post(request):
    return render(request,'create_post.html')