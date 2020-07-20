from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages # To Display Messages
from django.contrib.auth.decorators import login_required   # This is an Decorator Which Prevents access to the certain view without login
from django.contrib.auth.models import User # To Create User In database
from django.contrib.auth import authenticate, login, logout # To Login User In Data Base
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import profile

# Create your views here.

def index(request) :
    return render(request,'index.html',)

def register(request) :
    if request.user.is_authenticated :
        return redirect('error')
    else :
        if request.method == 'POST' :
            # Getting POST Data
            s_fname = request.POST['s_fname']
            s_lname = request.POST['s_lname']
            s_email = request.POST['s_email']
            s_phone = request.POST['s_phone']
            s_pass = request.POST['s_pass']
            s_cpass = request.POST['s_cpass']

        # Conditions For Input 
            if len(s_phone) < 10 or len(s_phone) > 10 :
                messages.error(request," Wrong Contact Number ")
            elif  s_pass != s_cpass : 
                messages.error(request," Both Password Must Be Same ")
            elif not s_fname.isalnum() or not s_lname.isalnum() :
                messages.error(request," Enter Correct Name ")
            else :
                # Creating new User Using create_user method 
                myuser = User.objects.create_user(s_email,s_email,s_pass)   #( username,email,password )
                myuser.first_name = s_fname
                myuser.last_name = s_lname
                myuser.save()
                messages.success(request,"Your Account Has Been Created Succesfully! Now You Can Login To Continue")
                return redirect('register')
            
        return render(request,'register.html',)


@login_required #Login Decorator Implemented !Go TO SETTINGS.py
def profile(request) :
    return render(request, 'profile.html')

@login_required
def user_profile_update(request) :
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }

    return render(request, 'user_profile_update.html', context)

def login_handel(request) :
    if request.method == 'POST' :
        # Getting POST Data
        login_email = request.POST['l_email']
        login_pass = request.POST['l_pass']

        # Passing Arguments to the username and password and creating user
        user = authenticate(username = login_email, password = login_pass)
        # Validating if user Exist
        if user is not None :
            # Checking User Data
            login(request,user)
            messages.success(request,"Login Succesfull")
            return redirect('index')
        else :
            messages.error(request,"Login Failed! Plaease Enter Your Credentials Correctly ")
            return redirect('register')

    # If Not Post Request Return 404  Error
    return redirect('error')  

@login_required
def logout_handel(request) :
    logout(request)
    messages.success(request,"You have Loged Out Succesfully")
    return redirect('register')

def error(request) :
    return render(request, 'error.html')


