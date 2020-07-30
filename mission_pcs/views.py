from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .models import staff,routine,time

def homepage(request):
    return render(request,"index.html")

def routineView(request):
    rt=routine.objects.all()
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    tm=time.objects.all()
    params={"routine":rt, "days":days,"times":tm}
    return render(request,"view.html", params)

def register(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        if staff(): 
            messages.info(request,"User Registered Successfully, Please Login!")
            stf = staff(name=name, mob=mobile, email=email, password=password)
            stf.save()
            return render(request, "login.html", context={
                'sent': True
            })
    else:
        return render(request, "register.html")

def timetable(request):
    if request.method == 'POST':
        subject=request.POST.get('subject')
        day=request.POST.get('day')
        start_time=request.POST.get('start_time')
        # end_time=request.POST.get('end_time')
        if routine(): 
            messages.info(request,"Added Successfully!")
            # stf = routine(subject=subject, day=day, start_time=start_time, end_time=end_time)
            stf = routine(subject=subject, day=day, start_time=start_time)
            stf.save()
            tm=time.objects.all()
            pr={"times":tm}
            return render(request, "time-table.html", context={
                'sent': True,"times":tm
            })
    else:
        tm=time.objects.all()
        pr={"times":tm}
        return render(request, "time-table.html",pr)

def login(request):
    if request.method == 'POST':
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        num_results = staff.objects.filter(mob=mobile, password=password).count()
        # print(num_results)
        if num_results>0:
            messages.info(request,"Login Successfully")
            tm=time.objects.all()
            return render(request, "time-table.html", context={
                'sent': True, "times":tm
            })
        else:
            messages.info(request,"Invalid Credentials")
            return render(request, "login.html", context={
                'sent': True
            })
        return render(request, "login.html")
    else:
        return render(request, "login.html")

def loginredirect(request):
    if request.method == 'POST':
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        num_results = staff.objects.filter(mob=mobile, password=password).count()
        # print(num_results)
        if num_results>0:
            messages.info(request,"Login Successfully")
            tm=time.objects.all()
            return render(request, "time-table.html", context={
                'sent': True, "times":tm
            })
        else:
            messages.info(request,"Invalid Credentials")
            return render(request, "login.html", context={
                'sent': True
            })
        return render(request, "login.html")
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")