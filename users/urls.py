from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    # 登录页面
    path('login/', views.login, name='login'),
    path('regist/', views.regist, name='regist'),
    path('logout/', views.logout, name='logout'),
]