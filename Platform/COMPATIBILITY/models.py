from django.db import models
from app01.models import Router

'''全量数据'''

'''
class Test(models.Model):
    # id = models.AutoField(primary_key=True) # 默认自增
    version = models.CharField(verbose_name="版本号", max_length=128)
    router = models.ForeignKey(verbose_name="路由器", to=Router, to_field='band', on_delete=models.SET_NULL, null=True,
                               blank=True)
    # router = models.CharField(verbose_name="路由器", max_length=128)
    case = models.CharField(verbose_name="测试样例", max_length=128)
    status_choices = (
        (0, "成功"),
        (1, "失败"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices)
    msg = models.CharField(verbose_name="日志信息", max_length=1024)
    elapsed = models.DateTimeField(verbose_name="运行时间")
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    environment_choice = (
        (4, "4楼"),
        (10, "10楼"),
    )
    environment = models.SmallIntegerField(verbose_name="测试环境", choices=environment_choice, null=True, blank=True)
    rssi = models.SmallIntegerField(verbose_name="信号强度", null=True, blank=True)
    channel = models.SmallIntegerField(verbose_name="信道序号", null=True, blank=True)
    bandwidth_choice = (
        (0, "20"),
        (1, "40"),
    )
    bandwidth = models.SmallIntegerField(verbose_name="信道带宽", choices=bandwidth_choice, null=True, blank=True)

    def __str__(self):
        return self.version  # 需要改一下
'''

'''吞吐测试'''

'''
class Throughput(models.Model):
    # id = models.AutoField(primary_key=True) # 默认自增
    version = models.CharField(verbose_name="版本号", max_length=128)
    router = models.ForeignKey(verbose_name="路由器", to=Router, to_field='band', on_delete=models.SET_NULL, null=True,
                               blank=True)
    # router = models.CharField(verbose_name="路由器", max_length=128)
    case = models.CharField(verbose_name="测试样例", max_length=128)
    standard = models.FloatField(verbose_name="测试标准")
    real = models.FloatField(verbose_name="实际测试")
    status_choices = (
        (0, "成功"),
        (1, "失败"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices)
    msg = models.CharField(verbose_name="日志信息", max_length=1024)
    elapsed = models.DateTimeField(verbose_name="运行时间")
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
'''

'''联网测试'''

'''
class Network(models.Model):
    # id = models.AutoField(primary_key=True) # 默认自增
    version = models.CharField(verbose_name="版本号", max_length=128)
    router = models.ForeignKey(verbose_name="路由器", to=Router, to_field='band', on_delete=models.SET_NULL, null=True,
                               blank=True)
    # router = models.CharField(verbose_name="路由器", max_length=128)
    case = models.CharField(verbose_name="测试样例", max_length=128)
    status_choices = (
        (0, "成功"),
        (1, "失败"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices)
    msg = models.CharField(verbose_name="日志信息", max_length=1024)
    elapsed = models.DateTimeField(verbose_name="运行时间")
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
'''

'''透传'''


class TT(models.Model):
    version = models.CharField(verbose_name="版本号", max_length=128, null=True, blank=True)
    # router = models.ForeignKey(verbose_name="路由器", to=Router, to_field='band', on_delete=models.SET_NULL, null=True,
    #                            blank=True)
    router = models.CharField(verbose_name="路由器", max_length=128)
    case = models.CharField(verbose_name="测试样例", max_length=128)
    category_choice = (
        (0, '联网'),
        (1, '吞吐'),
    )
    category = models.SmallIntegerField(verbose_name="类型", choices=category_choice)
    status_choices = (
        (0, "成功"),
        (1, "失败"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices)
    msg = models.CharField(verbose_name="日志信息", max_length=1024, null=True, blank=True)
    standard = models.FloatField(verbose_name="测试标准", null=True, blank=True)
    real = models.FloatField(verbose_name="实际测试", null=True, blank=True)
    elapsed = models.DateTimeField(verbose_name="运行时间")
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    environment_choice = (
        (4, "4楼"),
        (10, "10楼"),
    )
    environment = models.SmallIntegerField(verbose_name="测试楼层", choices=environment_choice, null=True,
                                           blank=True)
    rssi = models.SmallIntegerField(verbose_name="信号强度", null=True, blank=True)
    channel = models.SmallIntegerField(verbose_name="信道序号", null=True, blank=True)
    bandwidth_choice = (
        (0, "20M"),
        (1, "40M"),
        (3, "20/40M")
    )
    bandwidth = models.SmallIntegerField(verbose_name="信道带宽", choices=bandwidth_choice, null=True, blank=True)


'''IOT'''


class IOT(models.Model):
    version = models.CharField(verbose_name="版本号", max_length=128, null=True, blank=True)
    # router = models.ForeignKey(verbose_name="路由器", to=Router, to_field='band', on_delete=models.SET_NULL, null=True,
    #                            blank=True)
    router = models.CharField(verbose_name="路由器", max_length=128)
    case = models.CharField(verbose_name="测试样例", max_length=128)
    category_choice = (
        (0, '联网'),
        (1, '加密'),
        (2, '吞吐'),
    )
    category = models.SmallIntegerField(verbose_name="类型", choices=category_choice)
    # status_choices = (
    #     (0, "成功"),
    #     (1, "失败"),
    # )
    # status = models.SmallIntegerField(verbose_name="状态", choices=status_choices)
    status = models.BooleanField(verbose_name="状态")
    msg = models.CharField(verbose_name="日志信息", max_length=1024, null=True, blank=True)
    standard = models.FloatField(verbose_name="测试标准", null=True, blank=True)
    real = models.FloatField(verbose_name="实际测试", null=True, blank=True)
    elapsed = models.TimeField(verbose_name="执行时间")
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    environment_choice = (
        (4, "4楼"),
        (10, "10楼"),
    )
    environment = models.SmallIntegerField(verbose_name="测试楼层", choices=environment_choice, null=True,
                                           blank=True)
    rssi = models.SmallIntegerField(verbose_name="信号强度", null=True, blank=True)
    channel = models.SmallIntegerField(verbose_name="信道序号", null=True, blank=True)
    bandwidth_choice = (
        (0, "20M"),
        (1, "40M"),
        (3, "20/40M")
    )
    bandwidth = models.SmallIntegerField(verbose_name="信道带宽", choices=bandwidth_choice, null=True, blank=True)
