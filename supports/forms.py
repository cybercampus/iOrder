from django import forms

class RestaurantForm(forms.Form):

    opentime_choices = (
        (0, "8:00"),
        (1, "8:30"),
        (2, "9:00"),
        (3, "9:30"),
        (4, "10:00"),
        (5, "10:30"),
        (6, "11:00"),
    )
    closetime_choices = (
        (0, "16:00"),
        (1, "16:30"),
        (2, "17:00"),
        (3, "18:00"),
        (4, "19:00"),
        (5, "20:00"),
        (6, "21:00"),
        (7, "22:00"),
        (8, "23:00"),
        (9, "23:30"),
    )

    name = forms.CharField(max_length=20,label="餐馆名称",widget=forms.TextInput(attrs={'class': 'form-input'}))
    phonenumber = forms.CharField(max_length=20,label="联系电话",widget=forms.TextInput(attrs={'class': 'form-input'}))
    address = forms.CharField(max_length=100,label="餐馆地址",widget=forms.TextInput(attrs={'class': 'form-input'}))
    opentime = forms.IntegerField(label="营业时间", widget=forms.widgets.Select(choices=opentime_choices,
                                                               attrs={'class':'form-control form-input'}))
    closetime = forms.IntegerField(label="打烊时间", widget=forms.widgets.Select(choices=closetime_choices,
                                                               attrs={'class':'form-control form-input'}))
    pic = forms.ImageField(label='餐馆照片')