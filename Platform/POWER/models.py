from django.db import models

'''全量数据'''


class Test(models.Model):
    # id = models.AutoField(primary_key=True) # 默认自增
    version = models.CharField(verbose_name="版本号", max_length=128)
    router = models.CharField(verbose_name="路由器", max_length=64)
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


'''吞吐测试'''


class Throughput(models.Model):
    # id = models.AutoField(primary_key=True) # 默认自增
    version = models.CharField(verbose_name="版本号", max_length=128)
    router = models.CharField(verbose_name="路由器", max_length=64)
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



