# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
# def home_images(request):

#     return render(request,'index.html')
    # return HttpResponse('Welcome to the Moringa Tribune')from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from .models import Post, Parents, Child, Partners, Activities, Comments,Blog
from .forms import NewPostForm, RegChildForm,UpdateProForm,UpdateParForm,partnerForm,commentForm,NewBlogForm
from .forms import NewPostForm, RegChildForm,ActivityForm
# Create your views here.
# @login_required(login_url='/accounts/login/')
from .forms import NewPostForm, RegChildForm, UpdateProForm


def welcome(request):
    post = Post.objects.all()
    child = Child.objects.all()
    partners = Partners.objects.all()
    parent = Parents.objects.all() 
    blog =Blog.objects.all()
    return render(request, 'index.html', {'blog':blog,'post':post, 'child':child, 'partners':partners, 'parent':parent})


# login_required(login_url='/accounts/login')
def post(request, id):
    try:
        posts= Post.objects.get(id=id)
    except DoesNotExist:
        raise Http404
    return render(request, 'index.html',{'post':post})


# @login_required(login_url='/accounts/login')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('welcome')
    else:
        form = NewPostForm()
    return render (request, 'new_post.html', {"form":form})


@login_required(login_url='/accounts/login/')
def getProfile(request,users=None):
    user = request.user
    image = Parents.objects.filter(name=user)
    name = request.user
    profile = Parents.objects.filter(name=name).all()
    
    return render(request,'profile/profile.html',locals(),{"image":image})


@login_required(login_url='/accounts/login/')
def editProfile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProForm(request.POST,request.FILES)
        if form.is_valid():
            pics = form.save(commit=False)
            pics.user_name = current_user
            pics.save()
        return redirect('profile')

    else:
        form = UpdateProForm()
    return render(request,'profile/editProfile.html',{"test":form})


# @login_required(login_url='/accounts/login')
def child(request):
    current_user = request.user
    child = Child.objects.filter(parent=current_user).first()
    # parent = current_user
    return render(request, 'child.html',{'child':child, 'parent':parent})


# @login_required(login_url='/accounts/login')
def new_child(request):
    current_user = request.user
    if request.method == 'POST':
        form = RegChildForm(request.POST, request.FILES)
        if form.is_valid():
            child = form.save(commit=False)
            child.user = current_user
            child.save()
        return redirect('welcome')
    else:
        form = RegChildForm()
    return render (request, 'new_child.html', {"form":form})
# @login_required(login_url='/accounts/login')
# def Trainer(request):
#     current_user = request.user
#     trainer = Trainer.objects.filter(user=current_user).first()
#     return render(request, 'trainer.html',{'trainer':trainer})
# @login_required(login_url='/accounts/login')
# def new_Trainer(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = RegTrainerForm(request.POST, request.FILES)
#         if form.is_valid():
#             trainer = form.save(commit=False)
#             trainer.user = current_user
#             trainer.save()
#         return redirect('welcome')
#     else:
#         form = RegTrainerForm()
#     return render (request, 'new_trainer.html', {"form":form})
@login_required(login_url='/accounts/login/')
def getProfile(request,users=None):
    user = request.user
    parent_image = Parents.objects.filter(name=user)
    name = request.user
    profile = Parents.objects.filter(name=name).all()
    return render(request,'profile/profile.html',locals(),{"parent_image":parent_image})
@login_required(login_url='/accounts/login/')
def editProfile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProForm(request.POST,request.FILES)
        if form.is_valid():
            pics = form.save(commit=False)
            pics.user_name = current_user
            pics.save()
        return redirect('profile')
    else:
        form = UpdateProForm()
    return render(request,'profile/editProfile.html',{"test":form})

@login_required(login_url='/accounts/login/')
def pargetProfile(request,users=None):
    user = request.user
    parent_image = Partners.objects.filter(partner_name=user)
    name = request.user
    profile = Partners.objects.filter(partner_name=name).all()
    return render(request,'profile/partner_Profile.html',locals(),{"parent_image":parent_image})

@login_required(login_url='/accounts/login/')
def pareditProfile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateParForm(request.POST,request.FILES)
        if form.is_valid():
            pics = form.save(commit=False)
            pics.user_name = current_user
            pics.save()
        return redirect('parprofile')
    else:
        form = UpdateParForm()
    return render(request,'profile/pareditProfile.html',{"form":form})
# ============================

def username_present(request):
    user=request.user
    
    # current_user = request.user
    
    if request.method == 'POST':
        form = UpdateParForm(request.POST,request.FILES)
        if form.is_valid():
            pics = form.save(commit=False)
            pics.user = user
            pics.save()
            return redirect('parprofile')
    else:
        form = UpdateParForm()
    return render (request, 'profile/partn.html', {"form":form})
    
    # partner=Partners.objects.filter(partner_name=user)
    # if User.objects.filter(username=username).exists():
    #     return True
    
    # return False



def partners(request):
    current_user = request.user
    activities = Activities.objects.filter()
    partner= Partners.objects.filter(user=current_user).first()
    print(current_user)
    print(partner.approved)
    print(approved)
    message=None
    if partner is None:
        message= "you are not registered as a partnwer"
        # redirect(username_present)
        # if partner.approved == False:
        #     redirect("username_present")
 
    else:
        message= "Welcome to Azap Business View"

    return render(request,'partners.html',{ 'current_user':current_user, 'activities':activities, "message":message, "partner":partner})




def partners(request):
    current_user = request.user
    # activities = Activities.objects.filter()
    partner= Partners.objects.filter(user=current_user).first()
    print(current_user)
    
    act = Activities.objects.filter(partner_name=current_user.id).all()
    
    message=None
    # if partner is None:
        
    #     message= "you are not registered as a partner"
        
        # redirect(username_present)
        # if partner.approved == False:
        #     redirect("username_present")
    if partner.approved == False:
        
        message= "please check in 24 hours  "
    else:
        message= "Welcome to Azapp Business View"
       
    return render(request,'partners.html',{"act":act ,'current_user':current_user,  "message":message, "partner":partner})


# @login_required(login_url='/accounts/login/')
def new_event(request):
    current_user = request.user

    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = current_user
            event.save()
        return redirect('partner')
    else:
        form = ActivityForm()
    return render(request, 'new_event.html', {"form": form})


def subscribers(request,act_id):
    act = Activities.objects.filter(id=act_id).first()
    print(act)
    child = Child.objects.filter(activity_id=act.id)
    return render(request, 'subscribers.html', {"child": child,"act":act})



def dashboard(request):
    current_user = request.user
    comment = Comments.objects.filter(id = current_user.id).first()
    activities = Activities.objects.all()
    return render(request,'events.html',{ 'current_user':current_user, 'activities':activities, 'comment':comment})


# # @login_required(login_url='/accounts/login/')
# def partners(request):
#     current_user = request.user
#     # even = Activities.objects.filter(=even_id).first()
    
#     act = Activities.objects.filter(partner_name=current_user.id).all()
#     return render(request, 'partners.html', {"act":act})

# @login_required(login_url='/accounts/login/')
def activity(request):
    current_user = request.user
    # partner_name=Activities.objects.filter(partner_name=current_user.id).all()
    # even = Activities.objects.filter(=even_id).first()
    comment = Comments.objects.filter(id = current_user.id).first()
    acty = Activities.objects.all()
    # act = Activities.objects.filter(category=partner_name).all()
    return render(request, 'school.html', {'acty':acty})

@login_required(login_url='/accounts/login')
def comment(request, act_id):
    current_user = request.user
    act = Activities.objects.filter(id = act_id).first()
    parent = Parents.objects.filter(user = current_user.id).first()
    if request.method == 'POST':
        form = commentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.commented_by = parent
            comment.commented_act = act
            comment.save()
            return redirect('welcome')
    else:
        form = commentForm()
    return render(request, 'commentform.html', {'form': form, 'act_id':act_id})


@login_required(login_url='/accounts/login')
def blog(request):
    # try:
    #     blog= Blog.objects.all()
    # except DoesNotExist:
    #     raise Http404
    blog= Blog.objects.all()
    return render(request, 'blog.html',{'blog':blog})

@login_required(login_url='/accounts/login')
def new_blog(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = current_user
            blog.save()
        return redirect('welcome')
    else:
        form = NewBlogForm()
    return render (request, 'new_blog.html', {"form":form})