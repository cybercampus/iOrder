from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    # orders 的首页
    path('', views.order, name='index'),
    path('create/', views.CreateOrder, name='create'),
    path('edit<int:order_id>/', views.EditOrder, name='edit'),
    path('delete<int:order_id>/', views.DeleteOrder, name='delete'),
]