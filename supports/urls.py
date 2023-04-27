from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'supports'
urlpatterns = [
    # restaurant 的首页
    path('', views.Index, name='index'),
    path('create/', views.CreateRestaurant, name='create'),
]