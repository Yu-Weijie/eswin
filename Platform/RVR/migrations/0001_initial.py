# Generated by Django 3.2.18 on 2023-08-18 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=64, verbose_name='编号')),
                ('band', models.CharField(max_length=64, verbose_name='品牌')),
                ('chip', models.CharField(blank=True, max_length=128, null=True, verbose_name='芯片型号')),
                ('info', models.CharField(blank=True, max_length=256, null=True, verbose_name='详细信息')),
                ('status', models.SmallIntegerField(choices=[(1, '在线'), (2, '离线')], default='2', verbose_name='状态')),
            ],
            options={
                'verbose_name': '路由器',
                'verbose_name_plural': '路由器',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=128, verbose_name='版本号')),
                ('router', models.CharField(max_length=64, verbose_name='路由器')),
                ('case', models.CharField(max_length=128, verbose_name='测试样例')),
                ('status', models.SmallIntegerField(choices=[(0, '成功'), (1, '失败')], verbose_name='状态')),
                ('msg', models.CharField(max_length=1024, verbose_name='日志信息')),
                ('elapsed', models.DateTimeField(verbose_name='运行时间')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('environment', models.SmallIntegerField(blank=True, choices=[(4, '4楼'), (10, '10楼')], null=True, verbose_name='测试环境')),
                ('rssi', models.SmallIntegerField(blank=True, null=True, verbose_name='信号强度')),
                ('channel', models.SmallIntegerField(blank=True, null=True, verbose_name='信道序号')),
                ('bandwidth', models.SmallIntegerField(blank=True, choices=[(0, '20'), (1, '40')], null=True, verbose_name='信道带宽')),
            ],
        ),
        migrations.CreateModel(
            name='Throughput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=128, verbose_name='版本号')),
                ('router', models.CharField(max_length=64, verbose_name='路由器')),
                ('case', models.CharField(max_length=128, verbose_name='测试样例')),
                ('standard', models.FloatField(verbose_name='测试标准')),
                ('real', models.FloatField(verbose_name='实际测试')),
                ('status', models.SmallIntegerField(choices=[(0, '成功'), (1, '失败')], verbose_name='状态')),
                ('msg', models.CharField(max_length=1024, verbose_name='日志信息')),
                ('elapsed', models.DateTimeField(verbose_name='运行时间')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
            ],
        ),
    ]
