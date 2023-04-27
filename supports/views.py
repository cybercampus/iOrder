from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RestaurantForm
from .models import Restaurant
from users.models import User

def Index(request):
    ticket = request.COOKIES.get('ticket')
    if not ticket:
        return HttpResponseRedirect('/users/login/')
 
    user = User.objects.filter(ticket=ticket)
    if not user:
        return HttpResponseRedirect('/users/login/')

    rest_list = Restaurant.objects.all().order_by('-createdate')

    context = {'restaurants':rest_list,'username':request.COOKIES.get('username')}

    return render(request, 'supports/index.html', context)

def CreateRestaurant(request):
    username = request.COOKIES.get('username')
    if request.method == 'POST':
        # 创建 RestaurantForm 的实例
        form = RestaurantForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # 获取用户输入
            name = form.cleaned_data['name']
            phonenumber  = form.cleaned_data['phonenumber']
            address = form.cleaned_data['address']
            opentime = form.cleaned_data['opentime']
            closetime = form.cleaned_data['closetime']
            #pic = form.cleaned_data['pic']
            pic = request.FILES.get('pic')
            restaurant = Restaurant(name=name,phonenumber=phonenumber,address=address,opentime=opentime,closetime=closetime,pic=pic)

            restaurant.save()
            return HttpResponseRedirect('/supports/')
        else:
            error_msg = form.errors.as_data()
            render(request, 'supports/create.html', {'obj': form,'errors': error_msg,})

    # 如果 get 方式，就创建一个空白 Form 表单，或者需要编辑点餐数据时 在空白 Form 表单赋初始值
    else:
        username = request.COOKIES.get('username')

        #在创建 Form 的时候，给输入框赋初始值。
        form = RestaurantForm(initial={"opentime": 2,'closetime':7})   
        
    return render(request, 'supports/create.html', {'obj': form, 'username':username })
