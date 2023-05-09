from django.shortcuts import render, redirect
from .models import Blog, Myblog
from .forms import Blogform, CoustomUserRagister
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def ragisterPage(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are Already Logged In')
        return redirect('/')
    else:
        form = CoustomUserRagister()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "User Ragistered Successfully")
                return redirect('blogs')
        context = {'form': form}
        return render(request, 'accounts/ragister.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are Already Logged In')
        return redirect('/')
    else:
        if request.method == 'POST':
            lusername = request.POST.get('username')
            lpassword = request.POST.get('password')
            user = authenticate(
                request, username=lusername, password=lpassword)
            if user is not None:
                login(request, user)
                messages.success(request, 'Loged In Successfully')
                return redirect('/')
        return render(request, 'accounts/login.html')


def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.warning(request, 'Logout Successfully')
        return redirect('/')
    return render(request, 'accounts/login.html')


def home(request):
    return render(request, 'accounts/index.html')


def blogs(request):
    form = Blog.objects.all()
    context = {'form': form}
    return render(request, 'accounts/index.html', context)


def viewblog(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {'blog': blog}
    return render(request, 'accounts/layout/view.html', context)


def addblog(request):
    if request.user.is_authenticated:
        form = Blogform
        if request.method == 'POST':
            form = Blogform(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Blog Added Successfully")
                return redirect('blogs')
        context = {'form': form}
        return render(request, 'accounts/layout/add.html', context)
    else:
        return redirect('login')


def editBlog(request, pk):
    blog_id = Blog.objects.get(id=pk)
    form = Blogform(instance=blog_id)
    if request.method == 'POST':
        form = Blogform(request.POST, request.FILES, instance=blog_id)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog Updated Successfully")
            return redirect('blogs')
    context = {'form': form}
    return render(request, 'accounts/edit.html', context)


def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    messages.info(request, "Blog Deleted Succesfully")
    return redirect('blogs')


@login_required(login_url='login')
def myblog(request):
    blog = Blog.objects.filter(user=request.user)
    context = {'blog': blog}
    return render(request, 'accounts/myblog.html', context)
