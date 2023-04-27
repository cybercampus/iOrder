from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import OrderForm
from .models import Order
from users.models import User

def order(request):
    ticket = request.COOKIES.get('ticket')
    if not ticket:
        return HttpResponseRedirect('/users/login/')
 
    user = User.objects.filter(ticket=ticket)
    if not user:
        return HttpResponseRedirect('/users/login/')

    date_today = datetime.now().strftime('%Y-%m-%d')
    order_list = Order.objects.filter(createdate__gte = date_today).order_by('dinnertime','-createdate')
    paginator = Paginator(order_list, 5) # 一页显示 5 条数据
    page = request.GET.get('page')

    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是数字，则设置为第一页
        orders = paginator.page(1)
    except EmptyPage:
        # 如果页码超出页码范围，则设置为最后一页
        orders = paginator.page(paginator.num_pages)

    context = {'orders':orders,'username':request.COOKIES.get('username')}

    return render(request, 'orders/index.html', context)

def CreateOrder(request):
    ticket = request.COOKIES.get('ticket')
    username = request.COOKIES.get('username')
    if not ticket:
        return HttpResponseRedirect('/users/login/')
 
    user = User.objects.filter(ticket=ticket)
    if not user:
        return HttpResponseRedirect('/users/login/')

    if request.method == 'POST':
        # 创建 OrderForm 的实例
        form = OrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # 获取用户输入
            username = form.cleaned_data['username']
            createdate  = form.cleaned_data['createdate']
            dish = form.cleaned_data['dish']
            quantity = form.cleaned_data['quantity']
            spicy = form.cleaned_data['spicy']
            dinnertime = form.cleaned_data['dinnertime']
            order = Order(username=username,createdate=createdate,dish=dish,quantity=quantity,spicy=spicy,dinnertime=dinnertime)

            order.save()
            return HttpResponseRedirect('/orders/')
        else:
            error_msg = form.errors.as_data()
            render(request, 'orders/createorder.html', {'obj': form,'errors': error_msg,})

    # 如果 get 方式，就创建一个空白 Form 表单，或者需要编辑点餐数据时 在空白 Form 表单赋初始值
    else:
        username = request.COOKIES.get('username')

        #在创建 Form 的时候，给 username 输入框赋初始值。
        form = OrderForm(initial={"username": username,
            'createdate':datetime.now().strftime('%Y-%m-%d'),'quantity':1})   
        
    return render(request, 'orders/create.html', {'obj': form, 'username':username })

def EditOrder(request,order_id):
    ticket = request.COOKIES.get('ticket')
    if not ticket:
        return HttpResponseRedirect('/users/login/')
 
    user = User.objects.filter(ticket=ticket)
    if not user:
        return HttpResponseRedirect('/users/login/')

    if request.method == 'POST':
        # 创建 OrderForm 的实例
        form = OrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # 获取用户输入
            username = form.cleaned_data['username']
            createdate  = form.cleaned_data['createdate']
            dish = form.cleaned_data['dish']
            quantity = form.cleaned_data['quantity']
            spicy = form.cleaned_data['spicy']
            dinnertime = form.cleaned_data['dinnertime']
            
            order = Order.objects.filter(id=order_id).first()
            order.username = username
            order.dish = dish
            order.quantity = quantity
            order.spicy = spicy
            order.dinnertime = dinnertime

            order.save()
            return HttpResponseRedirect('/orders/')
        else:
            error_msg = form.errors.as_data()
            render(request, 'orders/createorder.html', {'obj': form,'errors': error_msg,})
    if request.method == 'GET':
        # 根据 order_id 获取 order 数据
        order = Order.objects.filter(id=order_id).first()
        username = order.username
        createdate = order.createdate
        dish = order.dish
        quantity = order.quantity
        spicy = order.spicy
        dinnertime = order.dinnertime
        
        form = OrderForm(initial={"username": username,
            'createdate':datetime.now().strftime('%Y-%m-%d'),
            'dish':dish,
            'quantity':quantity,
            'spicy':spicy,
            'dinnertime':dinnertime},)   

        return render(request, 'orders/create.html', {'obj': form, 'username':username })

def DeleteOrder(request,order_id):
    Order.objects.filter(id=order_id).delete()
    return HttpResponseRedirect('/orders/')