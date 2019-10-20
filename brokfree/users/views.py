from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from users.forms import signupform,loginform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
import time

def signup(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            ulist=User.objects.all()
            flag=False
            for i in ulist:
                if i.username==form.cleaned_data.get('username'):
                    flag=True
                    error = 'Username already exists'
                    break
                elif i.email==form.cleaned_data.get('email'):
                    flag=True
                    error='Email already exists for another account'
            if flag:
                return render(request,'signup.html',{'error':error})
            else:
                user=form.save()
                user.refresh_from_db()
                t=time.ctime()
                d=datetime.datetime.now().year
                date=t[:10]+' '+str(d)
                user.profile.first_name = form.cleaned_data.get('first_name')
                user.profile.last_name=form.cleaned_data.get('last_name')
                user.profile.mobile=form.cleaned_data.get('mobile')
                user.profile.date=date
                user.save()
                raw_pass=form.cleaned_data.get('password1')
                user=authenticate(username=user.username,password=raw_pass)
                login(request,user)
                return render(request, 'thank-you.html', {'message': 'Thank You for Signing up in Brokfree!'})
        else:
            return render(request,'signup.html')
    else:
        return render(request,'signup.html')

def manual(request):
    if request.method=='POST':
        form =loginform(request.POST)
        if form.is_valid():
            try:
                user=User.objects.get(email=form.cleaned_data.get('email'))
            except User.DoesNotExist:
                return render(request,'login.html',{'error':'User does not exist.'})
            raw_pass=form.cleaned_data.get('password')
            user=authenticate(username=user.username,password=raw_pass)
            if user:
                login(request,user)
                return redirect('/profile/')
            else:
                return render(request,'login.html',{'error':'Incorrect Password'})
    else:
        return render(request,'login.html')
            


@login_required(login_url='/login/')
def prof(request):
    user=User.objects.get(username=request.user.username)
    dic={'username':user.username,'email':user.email,'first_name':user.profile.first_name,'last_name':user.profile.last_name,'mobile':user.profile.mobile,'date':user.profile.date}
    return render(request,'view-profile.html',dic)

def log_out(request):
    logout(request)
    return redirect('/home/')
