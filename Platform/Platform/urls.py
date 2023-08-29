"""Platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from app01 import views
from COMPATIBILITY import views as iot_views

from django.views import static ##新增
from django.conf import settings ##新增
from django.conf.urls import url ##新增


urlpatterns = [
    path('', views.home, name="home"),  # ip+port访问方式重定向为admin视图
    path('admin/', admin.site.urls),    # 主页面

    # 监控大屏
    path('dashboard/', views.dashboard, name='dashboard'),
    # 可视化
    # path('chart/list/', views.chart_list),
    path('dashboard/bar/', views.dashboard_bar),
    path('dashboard/pie/', views.dashboard_pie),
    # path('chart/line/', views.chart_line),

    # path('upload/', views.upload, name='upload'),  之前单个设备测试上传
    path('connect/', views.connect, name="connect"), # 设备连接
    path('multi_upload/', views.multi_upload),  # 设备上传数据
    path('visualize/<str:uid>/', views.visualize),   # 每个设备单独信息可视化界面
    path('snr/line/<str:uid>/', views.snr_line),
    path('rssi/line/<str:uid>/', views.rssi_line),

    # path('test/', views.test),





    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),





]

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)