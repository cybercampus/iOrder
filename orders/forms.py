from django import forms
from supports.models import Dish

class OrderForm(forms.Form):
    dinnertime_choices = (
        (0,u'午饭'),
        (1,u'晚饭'),
    )

    spicy_choices = (
        (0, "免辣"),
        (1, "微辣"),
        (2, "中辣"),
        (3, "重辣"),
        (4, "超辣"),
    )

    #下单人  
    username = forms.CharField(label='订饭人',widget=forms.TextInput(attrs={'class': 'form-input'}),error_messages={'required':u'人名不能为空'})
     # 下单时间
    createdate = forms.DateField(label='订饭时间', widget=forms.DateTimeInput(attrs={'class': 'form-input','type':'date'}))
    # 购买菜品
    dish = forms.ModelChoiceField(label='菜品',queryset= Dish.objects.all(),error_messages={'required':u'菜品不能为空'})
    # 购买数量
    quantity = forms.IntegerField(label='数量', widget=forms.TextInput(attrs={'class': 'form-input','type':'number'}))
    # 麻辣程度
    spicy = forms.IntegerField(label='麻辣程度',widget=forms.widgets.Select(choices=spicy_choices,
                                                               attrs={'class':'form-control form-input'}))
    # 午饭还是晚饭
    dinnertime = forms.IntegerField(label='吃饭时间',widget=forms.widgets.Select(choices=dinnertime_choices,
                                                               attrs={'class':'form-control form-input'}))