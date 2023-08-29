from django.db import models

'''路由器管理'''


class Router(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(verbose_name="编号", max_length=32)  # 换成整型前端post add会报错 怀疑是simpleui的bug
    band = models.CharField(verbose_name="品牌", max_length=64, unique=True)
    name = models.CharField(verbose_name="名称", max_length=64, unique=True)
    chip = models.CharField(verbose_name="芯片型号", max_length=128, null=True, blank=True)  # null为数据库级别 blank为admin级别
    mode = models.CharField(verbose_name="支持模式", max_length=128, null=True, blank=True)
    security = models.CharField(verbose_name="支持加密模式", max_length=128, null=True, blank=True)
    bandwidth = models.CharField(verbose_name="支持带宽", max_length=128, null=True, blank=True)
    info = models.CharField(verbose_name="备注信息", max_length=256, null=True, blank=True)

    def __str__(self):
        return self.number  # 新增成功后的提示

    class Meta:
        verbose_name_plural = '路由器'
        verbose_name = '路由器'  # 新增成功后的提示
