# -*- coding: utf-8 -*-
#System libraries
from __future__ import unicode_literals
import datetime
import web
from web.form import notnull

#Django modules

from django.views import generic 
from django import forms
from django.template.context_processors import request
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.expressions import OrderBy
from django.shortcuts import render, redirect
from django.db import models
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout #Import for processing Login
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
#Home App modules
from vinesF.models import videoID
from models import video
from models import users
from models import UserProfile

# Create your views here.

def index(request):
    #RA = str(videoID)
    RA = video.objects.get(IdNo="1")
    return render(request,'vine/index.html', {"VidName":RA})
   
        
def Mol(request):
    Ras = video.objects.all().order_by('-IdNo')
    Pley = video.objects.get(IdNo="3")
    #Vix2= str(video.objects.filter(video.AddPath, IdNo="3"))
    #Vixa= video.objects.raw(" SELECT * FROM vinesF_video ")
   # Vix= Vixa.IdNo  (All attempt to display video from database)
    return render(request,'vine/late.html', {'action': "These are the latest videos", "VidNames":Ras, "play":Pley})


#class IndexView(generic.ListView):
   # template_name = 'vinesF/index.html'
   # context_object_name= 'latest_question_list'
   
#Injecting data to template trial 1 $$$$$%%%%%
def latest(request):
    Re = video.Date
    Re.sort(order_by = ['-is_recent'])
    return render(request, 'vine/latest.html', Re)
    #print Re
   # Recents = models.vidoe.Date
   # Recent = Recents.extra(order_by = ['-is_recent'])
   
#Injecting data to template trial 2 $$$$$%%%%%
class DetailView(generic.DetailView):
    model = video
    template_name = 'vine/latest.html'
    #def Latex(self):
     #   def get_queryset(self):
          #  """Return the last five published Video."""
           # return video.objects.order_by('-is_recent') [:5]
      
#########################Form FOR PROCESSING NewVid###################################
class AddVidForm(forms.Form):
    
    primaryName = forms.CharField(label="Name", max_length=100)
    Origin = forms.CharField(label="Origin", max_length=200)
    PreferredAudience = forms.CharField(label="Audience", max_length=40)
    Date = forms.DateField()
    Link = forms.CharField(label="Url for File",)
    #VPath= forms.CharField(label="VPath", max_length=200)
    AddPath= forms.CharField(label="File path", max_length=200)
#########################ENF OF FORM FOR PROCESSING NewVid ###################################    

#########################VIEW FOR PROCESSING NewVid###################################
@login_required   
def NewVid(request):
    if request.POST:
        form= AddVidForm(request.POST)
        if form.is_valid():
            primaryName= form.cleaned_data['primaryName']
            Origin= form.cleaned_data['Origin']
            PreferredAudience= form.cleaned_data['PreferredAudience']
            Date= form.cleaned_data['Date']
            Link= form.cleaned_data['Link']
            # VPath= form.cleaned_data['VPath']
            AddPath= form.cleaned_data['AddPath']
            
            FreshVid= video(primaryName=primaryName, Origin=Origin, PreferredAudience=PreferredAudience, Date=Date,  Link=Link, VPath="", AddPath=AddPath)
            
            FreshVid.save()
            
            return HttpResponse("New Video added")
        else:
            return render(request,'vine/Newvid.html', {'form':form})
    else:
        form= AddVidForm()
        return render(request,'vine/Newvid.html', {'form':form})
        
#########################End Of VIEW FOR PROCESSING NewVid ###################################            
            
##########################User creation form and Processing #########################################
            
class NewUserForm(forms.Form):
    Name= forms.CharField(max_length=100, label= "Name")
    login= forms.CharField(max_length=25, label= "Login")
    password= forms.CharField(max_length=100, label= "Password")
    password_bis = forms.CharField(label = "Password", widget = forms.PasswordInput)
    phone= forms.CharField(max_length=14, label= "Phone")
    Birthday= forms.DateField()
    #Last_connection= forms.DateField(label= "Last_connection")
    email= forms.EmailField(label ="Email" )
    #date_created = models.DateField(verbose_name="date_created", auto_now_add=True )
    
    def clean(self):
        cleaned_data= super (NewUserForm, self).clean()
        password= self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')
        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
        return self.cleaned_data
    
    
#########################VIEW FOR PROCESSING New User###################################
    
def NewUser(request):
    if request.POST:
        form= NewUserForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']  
            login= form.cleaned_data['login']
            password= form.cleaned_data['password']    
            phone= form.cleaned_data['phone']    
            Birthday= form.cleaned_data['Birthday']
            #Last_connection= form.clean_data['Last_connection']
            email= form.cleaned_data['email']
            FreshUser = User.objects.create_user(username = login, email =email, password=password)
            #FreshUser= users(Name=Name, login=login, password=password, phone=phone, Birthday=Birthday, email=email)
            #FreshUser= users(Name=Name, login=login, password=password, phone=phone, Birthday=Birthday, Last_connection=Last_connection, email=email)
            FreshUser.is_active = True    #switch off to enable email verification
            #FreshUser.last_name=Name
            FreshUser.save()
            Fresh= UserProfile(user_auth=FreshUser, phone=phone, Birthday=Birthday )
            Fresh.save()
            #return HttpResponseRedirect(reverse('public_empty'))
            return HttpResponse("New User Added")
        else:
            return render(request, 'vine/NewUser.html', {'form':form})
            
            
    else:
        form= NewUserForm()
        return render(request, 'vine/NewUser.html', {'form':form})

            
#########################END OF VIEW FOR PROCESSING NewUser ###########################################
        
#########################VIEW FOR PROCESSING LOGIN (error 22-01-2018)###################################


        
def connection(request):
    if request.POST:
        form= Form_connection(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            password= form.cleaned_data["password"]
            user= users(Name=username, password=password)
            if user:
                login(request, user)
                #return HttpResponse("You are now connected")

            else:
                return render(request, 'vine/connection.html', {'form' :form})
                
                
    else:
        form= Form_connection()
        return render(request, 'vine/connection.html', {'form' :form})
            
            
    #else:
        #form= Form_connection()
        #return render(request, 'email_messages/connection.html', {'form' :form})

class Form_connection(forms.Form):
    username= forms.CharField(label="Login")
    password= forms.CharField(label="Password", widget=forms.PasswordInput)
    def clean2(self):
        cleaned_data = super(Form_connection,self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if not users(Name=username, password=password):
            raise forms.ValidationError("Wrong Login or Password or Both")
            
        return self.cleaned_data
                
#########################END OF VIEW FOR PROCESSING LOGIN (error 22-01-2018)###################################

##########################Django assisted logout function################################################
def Logout(request):
    logout(request)
    return render(request, 'vine/Logout.html')
##########################END OF Django assisted logout function################################################
            
            
################################ENHANCED USING SIMPLE 2 FIELD FORM USER CREATION FORM####################################
    
class SignupForm(UserCreationForm):
    first_name= forms.CharField(max_length=30, required=False)
    last_name= forms.CharField(max_length=30, required=False)
    email= forms.CharField(max_length=222, help_text='Required feild, please input your email address')

    class meta:
        model= User
        fields= ('username', 'first_name', 'last_name', 'email', 'password')    



def Signup2(request):
    if request.method == 'POST':
        form= SignupForm(request.POST)
        if form.is_valid():
            form.is_active = True 
            form.save()
            username= form.cleaned_data.get('username')
            raw_password= form.cleaned_data.get('password1')
            user= authenticate(username=username, password=raw_password)
            if user:
                login=(request, user)
                return redirect('NewVid')
    else:
        form= SignupForm()
    return render(request, 'vine/signup.html', {'form':form})        

################################END OF ENHANCED USING SIMPLE 2 FIELD FORM USER CREATION FORM####################################

##################################################SIGNING IN##########################################################
#class SigninForm(forms.Form):
    #username= forms.CharField(max_length=100, label= "Name")
    #password= forms.CharField(label= "Password", widget = forms.PasswordInput)
class SigninForm(forms.Form):
    username = forms.CharField(max_length=100,label="username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super(SigninForm,self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Wrong login or password")
        return self.cleaned_data
   

def Signin(request):
    if request.method == 'POST':
        form= SigninForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            raw_password= form.cleaned_data.get('password')
            user= authenticate(username=username, password=raw_password)
            if user:
                login=(request, user)
            if request.GET.get('next') is not None:
                return redirect(request.GET['next'])   
            
                return redirect('NewVid')
    #if request.GET.get('next') is not None:
        #return redirect(request.GET['next'])
            #if not user:
               # return HttpResponse("Wrong Password or User.")
                
    else:
        form= SigninForm()
    return render(request, 'vine/Signin.html', {'form':form})   

##################################################END OF SIGNING IN##########################################################         
