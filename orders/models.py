from django.db import models
from supports.models import Dish

class Order(models.Model):
    def __str__(self):
        return self.username
        
    spicy_choices = (
        (0, "免辣"),
        (1, "微辣"),
        (2, "中辣"),
        (3, "重辣"),
        (4, "超辣"),
    )
    dinnertime_choices = (
        (0, "午餐"),
        (1, "晚餐"),
    )
    
    # 下单人
    username = models.CharField(max_length=50,blank=False)
    # 下单时间
    createdate = models.DateTimeField('order date')
    # 购买菜品
    dish = models.ForeignKey(Dish, on_delete=models.DO_NOTHING)
    # 购买数量
    quantity = models.IntegerField(default=1)
    # 麻辣程度
    spicy = models.SmallIntegerField(choices=spicy_choices,default=0)
    # 午饭还是晚饭
    dinnertime = models.SmallIntegerField(choices=dinnertime_choices,default=0)
