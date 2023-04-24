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
    paginator = Paginator(order_list, 5) # Show 5 contacts per page
    page = request.GET.get('page')

    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        orders = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        orders = paginator.page(paginator.num_pages)

    context = {'orders':orders,'username':request.COOKIES.get('username')}

    return render(request, 'orders/index.html', context)

def CreateOrder(request):
    if request.method == 'POST':
        # 创建 OrderForm 的实例
        form = OrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            # 获取用户输入
            data = user_input_obj.clean()
            return HttpResponseRedirect('/orders/')
        else:
            error_msg = form.errors.as_data()
            render(request, 'orders/createorder.html', {'obj': form,'errors': error_msg,})

    # 如果 get 方式，就创建一个空白 Form 表单
    else:
        username = request.COOKIES.get('username')
        form = OrderForm(initial={"username": username,'createdate':datetime.now().strftime('%Y-%m-%d'),'quantity':1})   #在创建 Form 的时候，给 username 输入框赋初始值。
        
    return render(request, 'orders/createorder.html', {'obj': form, 'username':username })