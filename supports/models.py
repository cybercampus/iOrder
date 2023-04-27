from django.db import models

#餐馆
class Restaurant(models.Model):
    def __str__(self):
        return self.name

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
        
    # 餐馆名称
    name = models.CharField(max_length=50, blank=False)

    # 联系电话
    phonenumber = models.CharField(max_length=50,blank=False)

    # 地址
    address = models.CharField(max_length=200)
    
    # 开业时间
    opentime = models.SmallIntegerField(choices=opentime_choices,default=4)
    # 打烊时间
    closetime = models.SmallIntegerField(choices=closetime_choices,default=5)
    #图片
    pic = models.ImageField(upload_to='pic/',null=True,blank=True, verbose_name='Photo of Restaurant')

    createdate = models.DateTimeField('date created',auto_now_add=True)


#菜品
class Dish(models.Model):
    def __str__(self):
        return self.name
        
    # 菜品名称
    name = models.CharField(max_length=50, blank=False)

    # 编号
    SN = models.CharField(max_length=10,blank=False)

    # 所属餐馆
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    # 描述信息
    description = models.TextField(blank=True)
    # 价格
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    # 在上架
    onshelf = models.BooleanField(default=True)
    # 可点晚餐
    supper = models.BooleanField(default=True)
    # 图片, 将上传的图片存储到 media下的 pic目录下,settings.py 设置 media 路径
    picture = models.ImageField(upload_to='pic/',verbose_name=u'图片地址')

    createdate = models.DateTimeField('date created',auto_now_add=True)
