from django.shortcuts import render
from django.http import HttpResponseRedirect
#import random
#from django.contrib import auth
#from django.contrib.auth.hashers import make_password,check_password
#from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
#from django.urls import reverse
import datetime

from .models import User

# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')

    if request.method == 'POST':
        # 如果登录成功，转到 order 页面
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # 查询用户是否在数据库中
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if password == user.password:
                ticket = time = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')   
                response = HttpResponseRedirect('/orders/')     #转到 order 页面
                #max_age 存活时间(秒)
                response.set_cookie('ticket', ticket, max_age=10000)
                response.set_cookie('username', username, max_age=10000)
                # 存在服务端
                user.ticket = ticket
                user.save() #保存
                #response.user = user
                return response
            else:
                return render(request, 'users/login.html', {'error': '用户密码错误'})
        else:
            return render(request, 'users/login.html', {'error': '用户不存在'})

# 注册
def regist(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    if request.method == 'POST':
        # 注册
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 对密码进行加密
        # 查询用户是否在数据库中
        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'error': '用户已存在', 'username':username})
        else:
            User.objects.create(username=username, password=password)
            return HttpResponseRedirect('/users/login')


# 退出
def logout(request):
    request.session.clear()    #清除 session
    response = HttpResponseRedirect('/users/login/')
    response.delete_cookie("username")  #清除 coolie
    response.delete_cookie('ticket')
    return response