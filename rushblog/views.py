from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .form import SignUp,Login,PostForm,AddComment
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from .models import Post,Comment

def home(request):
    posts = Post.objects.all()
    return render(request, 'html/home.html',{'posts':posts})

def contact(request):
    return render(request, 'html/contact.html')

def user_signup(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            messages.success(request,'Welcome ')
            user = form.save()
            group = Group.objects.get(name="Subscriber")
            user.groups.add(group)
    else:
        form = SignUp()
    return render(request, 'html/signup.html', {'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = Login(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully !!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = Login()
        return render(request, 'html/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        gps = user.groups.all()
        full_name = user.get_full_name()
        return render(request, 'html/dashboard.html',{'posts':posts,'name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')

def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                content=form.cleaned_data['content']
                pst=Post(title=title,content=content)
                pst.save()
                form = PostForm()
        else:
            form = PostForm()
            return render(request,'html/addpost.html',{'form':form})
        messages.success(request,'Added Post !!')
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

def add_comment(request,id):
    if request.method=='POST':
        form = AddComment(request.POST)
        if form.is_valid():
            post=Post.objects.get(pk=id)
            name=form.cleaned_data['name']
            com=form.cleaned_data['com']
            cmt=Comment(post=post,name=name,com=com)
            cmt.save()
            form = AddComment()
    else:
        form = AddComment()
        return HttpResponseRedirect(f'/readpost/{id}')
    messages.success(request,'Added Comment !!')
    return HttpResponseRedirect(f'/readpost/{id}')

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
            return render(request,'html/updatepost.html',{'form':form})
        messages.success(request,'Updated Post !!')
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

def read_post(request,id):
    pi = Post.objects.get(pk=id)
    posts = Post.objects.all()
    form = AddComment()
    return render(request, 'html/readpost.html',{'postid':pi,'posts':posts,'form':form})