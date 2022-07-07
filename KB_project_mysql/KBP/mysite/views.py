from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.contrib.auth.hashers import make_password

def signup(request):

    if request.method == "POST":
        print(request.POST)
        username = request.POST["email"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_check = request.POST["password_check"]

        if password == password_check:
            user = User.objects.create_user(username, email, password)    #장고에서 추천하는 유저생성 방식
            user.password_check = make_password(password_check) #비밀번호 암호화 mysql에서 컬럼 사이즈변경
            user.save()
            return render(request, 'mysite/signin.html')
        else:
            return render(request, 'mysite/signup.html') 

    return render(request, 'mysite/signup.html')

def signin(request):
    return render(request, 'mysite/signin.html')

def Home(request):
    return HttpResponse("홈화면입니다.")