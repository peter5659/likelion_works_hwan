from django.shortcuts import render,redirect
from . import urls
from django.contrib.auth.models import User #user관련(생성)
from django.contrib import auth # 접근(login)
def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['passwordCheck']:
            try:
                user = User.objects.get(username= request.POST['username']) #너가 친 name이 이미 있는 username이라면
                return render(request, "signup.html",{'error': "username has already taken"}) #signup.html띄우고 error표시
            except: # 위에서 error가 나지 않았다면 생성해줘야지
                user= User.objects.create_user(
                    request.POST["username"],password=request.POST["password"])
                auth.login(request, user)
                return redirect('/')
        else:
            return render(request, "signup.html", {'error': "password is invalid"})
    else:
        return render(request, "signup.html")

def login(request):
    if request.method =="POST":
        user= auth.authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, "login.html", {'error': "ID or PW is invalid"})
    else:
        return render(request, "login.html")
# Create your views here.

def logout(request):
    if request.method =="POST":
        auth.logout(request)
        return redirect('/')
    else:
        return render(request, "signup.html")
