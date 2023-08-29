from django.db import models
from django.contrib.auth.models import User

'''Smoke'''


class Smoke(models.Model):
    project_choice = (
        (0, "版本烧录"),
        (1, "栈检查"),
        (2, "版本号"),
        (3, "wifi连接"),
        (4, "ble连接"),
        (5, "吞吐")
    )
    project = models.SmallIntegerField(verbose_name="测试项", choices=project_choice)
    sub_project = models.CharField(verbose_name="测试子项", max_length=64)
    level = models.CharField(verbose_name="用例等级", default="L0", max_length=16)
    preset_conditions = models.CharField(verbose_name="预置条件", max_length=256, null=True, blank=True)
    step = models.TextField(verbose_name="测试步骤", null=True, blank=True)
    expected_results = models.CharField(verbose_name="预期结果", max_length=128)
    is_execute = models.BooleanField(verbose_name="是否执行")
    notes = models.TextField(verbose_name="测试备注", null=True, blank=True)
    executor = models.ForeignKey(verbose_name="执行人", to=User, on_delete=models.SET_NULL, null=True, blank=True)
    auto = models.BooleanField(verbose_name="自动化")
    time = models.DateTimeField(verbose_name="时间", auto_now=True)


'''WIFI_STA'''


class WifiSta(models.Model):
    number = models.CharField(verbose_name="用例编号", max_length=64)
    category_choice = (
        (0, 'ASSOC'),
        (1, 'fastconnect'),
        (2, 'IPERF'),
        (3, 'OFDMA'),
        (4, 'QoS'),
        (5, 'ROAMING'),
    )
    category = models.SmallIntegerField(verbose_name="测试分类", choices=category_choice)
    project = models.CharField(verbose_name="测试项", max_length=64)
    sub_project = models.CharField(verbose_name="测试子项", max_length=128)
    level_choice = (
        (0, 'L0'),
        (1, 'L1'),
        (2, 'L2'),
        (3, 'L3')
    )
    level = models.SmallIntegerField(verbose_name='用例等级', choices=level_choice)
    preset_conditions = models.CharField(verbose_name="预置条件", max_length=256, null=True, blank=True)
    step = models.TextField(verbose_name="测试步骤", null=True, blank=True)
    expected_results = models.CharField(verbose_name="预期结果", max_length=128)
    is_execute = models.BooleanField(verbose_name="是否执行")
    notes = models.TextField(verbose_name="测试备注", null=True, blank=True)
    executor = models.ForeignKey(verbose_name="执行人", to=User, on_delete=models.SET_NULL, null=True, blank=True)
    auto = models.BooleanField(verbose_name="自动化")
    time = models.DateTimeField(verbose_name="时间", auto_now=True)


'''WIFI_AP'''


class WifiAp(models.Model):
    number = models.CharField(verbose_name="用例编号", max_length=64)
    category_choice = (
        (0, 'AP_STA'),
        (1, 'ASSOC'),
        (2, 'deauth'),
        (3, 'Gateway'),
        (4, 'IPERF'),
        (5, 'multi_sofap'),
        (6, 'QoS'),
        (7, 'STA&AP'),
        (8, 'STA_AP'),
    )
    category = models.SmallIntegerField(verbose_name="测试分类", choices=category_choice)
    project = models.CharField(verbose_name="测试项", max_length=64)
    sub_project = models.CharField(verbose_name="测试子项", max_length=128)
    level_choice = (
        (0, 'L0'),
        (1, 'L1'),
        (2, 'L2'),
        (3, 'L3')
    )
    level = models.SmallIntegerField(verbose_name='用例等级', choices=level_choice)
    preset_conditions = models.CharField(verbose_name="预置条件", max_length=256, null=True, blank=True)
    step = models.TextField(verbose_name="测试步骤", null=True, blank=True)
    expected_results = models.CharField(verbose_name="预期结果", max_length=128)
    is_execute = models.BooleanField(verbose_name="是否执行")
    notes = models.TextField(verbose_name="测试备注", null=True, blank=True)
    executor = models.ForeignKey(verbose_name="执行人", to=User, on_delete=models.SET_NULL, null=True, blank=True)
    auto = models.BooleanField(verbose_name="自动化")
    time = models.DateTimeField(verbose_name="时间", auto_now=True)


'''WIFI_Delay'''


class WifiDelay(models.Model):
    number = models.CharField(verbose_name="用例编号", max_length=64)
    category_choice = (
        (0, 'ap&sta_ping'),
        (1, 'ap_ping'),
        (2, 'sta_assoc_rate'),
        (3, 'sta_assoc_time'),
        (4, 'sta_longping'),
        (5, 'sta_ping'),
    )
    category = models.SmallIntegerField(verbose_name="测试分类", choices=category_choice)
    project = models.CharField(verbose_name="测试项", max_length=64)
    sub_project = models.CharField(verbose_name="测试子项", max_length=128)
    level_choice = (
        (0, 'L0'),
        (1, 'L1'),
        (2, 'L2'),
        (3, 'L3')
    )
    level = models.SmallIntegerField(verbose_name='用例等级', choices=level_choice)
    preset_conditions = models.CharField(verbose_name="预置条件", max_length=256, null=True, blank=True)
    step = models.TextField(verbose_name="测试步骤", null=True, blank=True)
    expected_results = models.CharField(verbose_name="预期结果", max_length=128)
    is_execute = models.BooleanField(verbose_name="是否执行")
    notes = models.TextField(verbose_name="测试备注", null=True, blank=True)
    executor = models.ForeignKey(verbose_name="执行人", to=User, on_delete=models.SET_NULL, null=True, blank=True)
    auto = models.BooleanField(verbose_name="自动化")
    time = models.DateTimeField(verbose_name="时间", auto_now=True)


'''WIFI_ThroughPut'''


class WifiThroughPut(models.Model):
    number = models.CharField(verbose_name="用例编号", max_length=64)
    category_choice = (
        (0, 'AP__Normal'),
        (1, 'AP_Normal'),
        (2, 'ax 5个 sta吞吐'),
        (3, 'ax 8个 sta吞吐'),
        (4, 'bgn 5个 sta吞吐'),
        (5, 'bgn 8个 sta吞吐'),
        (6, 'softap连接AP 8sta吞吐'),
        (7, 'STA&AP_Normal'),
        (8, 'sta_VeryStrong'),
        (9, 'sta_Weak'),
    )
    category = models.SmallIntegerField(verbose_name="测试分类", choices=category_choice)
    project = models.CharField(verbose_name="测试项", max_length=64)
    sub_project = models.CharField(verbose_name="测试子项", max_length=128)
    level_choice = (
        (0, 'L0'),
        (1, 'L1'),
        (2, 'L2'),
        (3, 'L3')
    )
    level = models.SmallIntegerField(verbose_name='用例等级', choices=level_choice)
    preset_conditions = models.CharField(verbose_name="预置条件", max_length=256, null=True, blank=True)
    step = models.TextField(verbose_name="测试步骤", null=True, blank=True)
    expected_results = models.CharField(verbose_name="预期结果", max_length=128)
    is_execute = models.BooleanField(verbose_name="是否执行")
    notes = models.TextField(verbose_name="测试备注", null=True, blank=True)
    executor = models.ForeignKey(verbose_name="执行人", to=User, on_delete=models.SET_NULL, null=True, blank=True)
    auto = models.BooleanField(verbose_name="自动化")
    time = models.DateTimeField(verbose_name="时间", auto_now=True)



'''WIFI_FT'''


class WifiFT(models.Model):
    number = models.CharField(verbose_name="用例编号", max_length=64)
    category_choice = (
        (0, 'ap&sta_Distance'),
        (1, 'ap_Distance'),
        (2, 'Complex'),
        (3, 'Distance'),
        (4, 'Normal'),
        (5, 'VeryComplex'),
    )
    category = models.SmallIntegerField(verbose_name="测试分类", choices=category_choice)
    project = models.CharField(verbose_name="测试项", max_length=64)
    sub_project = models.CharField(verbose_name="测试子项", max_length=128)
    level_choice = (
        (0, 'L0'),
        (1, 'L1'),
        (2, 'L2'),
        (3, 'L3')
    )
    level = models.SmallIntegerField(verbose_name='用例等级', choices=level_choice)
    preset_conditions = models.CharField(verbose_name="预置条件", max_length=256, null=True, blank=True)
    step = models.TextField(verbose_name="测试步骤", null=True, blank=True)
    expected_results = models.CharField(verbose_name="预期结果", max_length=128)
    is_execute = models.BooleanField(verbose_name="是否执行")
    notes = models.TextField(verbose_name="测试备注", null=True, blank=True)
    executor = models.ForeignKey(verbose_name="执行人", to=User, on_delete=models.SET_NULL, null=True, blank=True)
    auto = models.BooleanField(verbose_name="自动化")
    time = models.DateTimeField(verbose_name="时间", auto_now=True)




'''BLE'''


class Ble(models.Model):
    number = models.CharField(verbose_name="用例编号", max_length=64)
    category_choice = (
        (0, None),
        (1, 'CMD模式'),
        (2, 'Distance'),
        (3, '配网应用'),
    )
    category = models.SmallIntegerField(verbose_name="测试分类", choices=category_choice)
    project = models.CharField(verbose_name="测试项", max_length=64)
    sub_project = models.CharField(verbose_name="测试子项", max_length=128)
    level_choice = (
        (0, 'L0'),
        (1, 'L1'),
        (2, 'L2'),
        (3, 'L3')
    )
    level = models.SmallIntegerField(verbose_name='用例等级', choices=level_choice)
    preset_conditions = models.CharField(verbose_name="预置条件", max_length=256, null=True, blank=True)
    step = models.TextField(verbose_name="测试步骤", null=True, blank=True)
    expected_results = models.CharField(verbose_name="预期结果", max_length=128)
    is_execute = models.BooleanField(verbose_name="是否执行")
    notes = models.TextField(verbose_name="测试备注", null=True, blank=True)
    executor = models.ForeignKey(verbose_name="执行人", to=User, on_delete=models.SET_NULL, null=True, blank=True)
    auto = models.BooleanField(verbose_name="自动化")
    time = models.DateTimeField(verbose_name="时间", auto_now=True)


'''BLE_MESH'''


class BleMesh(models.Model):
    number = models.CharField(verbose_name="用例编号", max_length=64)
    category_choice = (
        (0, "BLE MESH BEARER"),
        (1, 'BLE MESH FEATURE'),
        (2, 'BLE MESH MODEL'),
        (3, '灯控（CLI指令）'),
        (4, '动态log level'),
        (5, '设备角色设置及feature组合')
    )
    category = models.SmallIntegerField(verbose_name="测试分类", choices=category_choice)
    project = models.CharField(verbose_name="测试项", max_length=64)
    sub_project = models.CharField(verbose_name="测试子项", max_length=128)
    level_choice = (
        (0, 'L0'),
        (1, 'L1'),
        (2, 'L2'),
        (3, 'L3')
    )
    level = models.SmallIntegerField(verbose_name='用例等级', choices=level_choice)
    preset_conditions = models.CharField(verbose_name="预置条件", max_length=256, null=True, blank=True)
    step = models.TextField(verbose_name="测试步骤", null=True, blank=True)
    expected_results = models.CharField(verbose_name="预期结果", max_length=128)
    is_execute = models.BooleanField(verbose_name="是否执行")
    notes = models.TextField(verbose_name="测试备注", null=True, blank=True)
    executor = models.ForeignKey(verbose_name="执行人", to=User, on_delete=models.SET_NULL, null=True, blank=True)
    auto = models.BooleanField(verbose_name="自动化")
    time = models.DateTimeField(verbose_name="时间", auto_now=True)