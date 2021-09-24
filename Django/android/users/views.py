from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def index(request):
    return HttpResponse("Hello,You're at the login index.")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            return HttpResponse('用户登录成功')
        return HttpResponse('用户名或密码错误！')
