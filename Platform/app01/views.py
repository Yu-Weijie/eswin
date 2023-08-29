import time

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Router
from POWER.models import Test
import datetime
import random


# Create your views here.


def chart(request):
    return render(request, 'chart_list.html')


def dashboard(request):
    user_count = User.objects.count()  # 获取所有用户数量
    router_count = Router.objects.count() # 获取所有路由器数量
    offline_count = router_count - 1
    context = {'user_count': user_count,
               'router_count': router_count,
               'offline_count': offline_count,
               }
    return render(request, 'dashboard.html', context)


def home(request):
    return redirect('admin/')  # http://127.0.0.1:8000 这种方式直接访问的话 重定向为 http://127.0.0.1:8000/admin/


def dashboard_bar(request):
    '''柱状图数据'''
    legend = ['xx', 'xxx']
    series_list = [
        {
            "name": 'xx',
            "type": 'bar',
            "data": [5, 20, 36, 10, 10, 20]
        },
        {
            "name": 'xxx',
            "type": 'bar',
            "data": [35, 20, 32, 40, 15, 50]
        }
    ]
    x_axis = ['1', '2', '3', '4', '5', '6']

    result = {
        'status': True,
        'data': {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)


'''成功/失败的样例数量'''
def dashboard_pie(request):
    success_count = Test.objects.filter(status=0).count() # 成功样例数量
    fail_count = Test.objects.filter(status=1).count() # 失败样例的数量
    result = {
        'status': True,
        'data': [
            {"value": success_count, "name": '成功'},
            {"value": fail_count, "name": '失败'},
        ]
    }
    return JsonResponse(result)


def chart_line(request):
    result = {
        'status': True,
        'data': {
            'snr': snr,
        }
    }
    return JsonResponse(result)


# 单个点击"可视化按钮"访问的视图
def snr_line(request, uid):
    result = {
        'status': True,
        'data': {
            'snr': snr_db[uid],
        }
    }
    return JsonResponse(result)


def rssi_line(request, uid):
    result = {
        'status': True,
        'data': {
            'rssi': rssi_db[uid],
        }
    }
    return JsonResponse(result)



# 上传数据(单终端方案)
# snr = [20, 20, 23, 35, 21, 46, 12, 24, 32]
# def upload(request):
#     if request.method == 'POST':
#         new_snr = request.POST.get('snr')
#         snr.pop(0)
#         snr.append(new_snr)
#         result = {
#             'status': True,
#             'data': {
#                 'snr': snr,
#             }
#         }
#         return JsonResponse(result)


client_time_db = {}
# 上传数据(多终端方案)
def multi_upload(request):
    if request.method == 'POST':
        unique_code = request.POST.get('unique_code')
        new_snr = request.POST.get('snr')
        new_rssi = request.POST.get('rssi')
        snr_db[unique_code].pop(0)
        snr_db[unique_code].append(new_snr)
        rssi_db[unique_code].pop(0)
        rssi_db[unique_code].append(new_rssi)
        client_time = request.POST.get('client_time')
        client_time_db[unique_code] = client_time
        return HttpResponse("OK")


# 处理连接请求

# 存储方式
snr_db = {}
rssi_db = {}


def connect(request):
    if request.method == "POST":
        # 判断设备是否在资产列表中
        unique_code = request.POST.get('unique_code')
        exists = Property.objects.filter(unique_code=unique_code).exists()
        if exists:
            # 是否携带连接标识
            connect_flag = request.POST.get('connect_flag')
            if connect_flag:
                # 将信息入Equipment表
                category = request.POST.get('category')
                ip = request.POST.get('ip')
                mac = request.POST.get('mac')
                ssid = request.POST.get('ssid')
                start_time = datetime.datetime.now()
                print(category)
                print(ip)
                print(mac)
                # 设备连接成功后为其创建字段，将记录存入数据库中
                new_equipment = Equipment(
                    uid=unique_code,
                    category=category,
                    ip=ip,
                    mac=mac,
                    ssid=ssid,
                    start_time=start_time)
                new_equipment.save()
                # 更新资产管理的设备状态
                Property.objects.filter(unique_code=unique_code).update(status="1")

                # 初始化snr的存放
                snr_db[unique_code] = [0] * 24
                # 初始化rssi存放
                rssi_db[unique_code] = [0] * 24
                return HttpResponse(status=200)  # 安全性考虑，后期需要中间件进行阻断
    return HttpResponse(status=403)


def visualize(request, uid):
    return render(request, "visualization.html", {'uid': uid})


# from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import DjangoJobStore, register_job
#
# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")

# 每三秒执行一次定时任务
# @register_job(scheduler, "interval", seconds=3, id=str(random.randint(0, 100000000)))
# def check_alive():
#     if len(client_time_db) != 0:
#         time_out_uid = []  # 超时设备列表
#         server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         server_time = datetime.datetime.strptime(server_time, '%Y-%m-%d %H:%M:%S')
#         for uid, time_str in client_time_db.items():
#             client_time = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
#             interval = (server_time - client_time).seconds # 计算服务器当前时间和客户端最新时间的差值
#             if interval > 5:
#                 time_out_uid.append(uid)
#         for uid in time_out_uid:
#             Equipment.objects.filter(uid=uid).delete() # 删除数据库simulation下Equipment表中的该uid记录
#             Property.objects.filter(unique_code=uid).update(status="2") # 修改"资产管理"的设备状态
#             # client_time_db.pop(uid) # 清空字典中关于该uid的时间
#             del client_time_db[uid]
# scheduler.start()



# def test(request):
#     ssid = request.POST.get('ssid')
#     ip = request.POST.get('ip')
#     print(ssid)
#     print(ip)
#     print("******************** OK ***********************")
#     return HttpResponse(status=200)
