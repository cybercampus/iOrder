from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    # orders 的首页
    path('', views.order, name='index'),
    path('createorder/', views.CreateOrder, name='createorder'),
    #path('<int:pk>/', views.DetailView.as_view(), name='order'),
]