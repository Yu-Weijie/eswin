from django.contrib import admin

# Register your models here.


# tasks/admin.py
from django.contrib import admin
from django.shortcuts import render, redirect

# admin.site.site_header = 'ESWIN测试系统'  # 设置header
# admin.site.site_title = 'ESWIN测试系统'  # 设置title
# admin.site.index_title = 'ESWIN测试系统'

from .models import *

# admin.site.register(Equipment)

# admin文件中定义展示页面，后续方便页面管理，可以独立文件，通过import方式引入进行注册
# from myapp.models import job_detail

'''
@admin.register(Test)
class Test(admin.ModelAdmin):
    # 设置页面可以展示的字段
    list_display = ('version', 'router', 'case', 'status', 'msg', 'elapsed', 'start_time', 'end_time', 'environment', 'rssi', 'channel', 'bandwidth')
    # 默认不配置的话，第一个字段会存在链接到记录编辑页面
    # list_display_links = None
    # list_display_links = ('uid',)
    # 设置过滤选项
    list_filter = ('version', 'router', 'status', 'environment')
    # 每页显示条目数 缺省值100
    list_per_page = 15
    # show all页面上的model数目，缺省200
    list_max_show_all = 200
    # 设置可编辑字段 如果设置了可以编辑字段，页面会自动增加保存按钮
    # list_editable = ('IN_PARA_COMMENT',)
    # 按日期月份筛选 该属性一般不用
    # date_hierarchy = 'CREATED_TIME'
    # 按连接时间降序排序
    ordering = ('-end_time',)
    # 搜索条件设置
    # search_fields = ('version',)

    # 增加自定义按钮
    # actions = ['visualization']
    #
    # def visualization(self, request, queryset):
    #     print(queryset[0])
    #     return redirect("/visualize/" + str(queryset[0]) + "/")

    # 显示的文本，与django admin一致
    # visualization.short_description = '可视化'
    # icon，参考element-ui icon与https://fontawesome.com
    # visualization.icon = 'fas fa-audio-description'
    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    # visualization.type = 'danger'
    # 给按钮追加自定义的颜色
    # custom_button.style = 'color:black;'
    # visualization.action_type = 0
    # visualization.action_url = 'show/'

    # 表头字段显示中文名称，这里需要修改models文件，在定义字段的时候增加别名
    # eg1：JOB_NAME = models.CharField('任务名称',max_length=128)
    # eg2: name = models.CharField(max_length=30,verbose_name=u"姓名")

    # 字段关联展示
    ## 场景1、关联其他表的数据展示，此处外键展示不做演示，生产环境尽量减少外键使用

    ## 场景2、枚举信息转义展示
    ###  此处需要在model定义页面通过枚举值转义配置对应展示中文信息,参考model模块代码设置

     # """
     #   这种禁用编辑链接的放法只是不让它在页面中显示，即把超链接去掉了，
     #   但是还是可以通过手动输入url的方式来进入编辑页面。
     #   不过可以配合设置fieldsets或者readonly_fieldss来达到目的
     #   注意：这里建议删除按钮要禁用掉，否则只有拥有view权限的人员依然可以进行删除动作，或者需要进行人员角色判断
     # """

    def has_add_permission(self, request):
        # 禁用添加按钮
        return True

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return True

@admin.register(Throughput)
class Throughput(admin.ModelAdmin):
    # 设置页面可以展示的字段
    list_display = ('version', 'router', 'case', 'standard', 'real', 'status', 'msg', 'elapsed', 'start_time', 'end_time')
    # 默认不配置的话，第一个字段会存在链接到记录编辑页面
    list_display_links = None
    # list_display_links = ('uid',)
    # 设置过滤选项
    list_filter = ('version', 'router', 'case', 'status')
    # 每页显示条目数 缺省值100
    list_per_page = 15
    # show all页面上的model数目，缺省200
    list_max_show_all = 200
    # 设置可编辑字段 如果设置了可以编辑字段，页面会自动增加保存按钮
    # list_editable = ('IN_PARA_COMMENT',)
    # 按日期月份筛选 该属性一般不用
    # date_hierarchy = 'CREATED_TIME'
    # 按连接时间降序排序
    ordering = ('-end_time',)
    # 搜索条件设置
    # search_fields = ('msg',)

    # 增加自定义按钮
    actions = ['visualization']

    def visualization(self, request, queryset):
        print(queryset[0])
        return redirect("/visualize/" + str(queryset[0]) + "/")

    # 显示的文本，与django admin一致
    visualization.short_description = '可视化'
    # icon，参考element-ui icon与https://fontawesome.com
    # visualization.icon = 'fas fa-audio-description'
    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    visualization.type = 'danger'
    # 给按钮追加自定义的颜色
    # custom_button.style = 'color:black;'
    # visualization.action_type = 0
    # visualization.action_url = 'show/'

    # 表头字段显示中文名称，这里需要修改models文件，在定义字段的时候增加别名
    # eg1：JOB_NAME = models.CharField('任务名称',max_length=128)
    # eg2: name = models.CharField(max_length=30,verbose_name=u"姓名")

    # 字段关联展示
    ## 场景1、关联其他表的数据展示，此处外键展示不做演示，生产环境尽量减少外键使用

    ## 场景2、枚举信息转义展示
    ###  此处需要在model定义页面通过枚举值转义配置对应展示中文信息,参考model模块代码设置

     # """
     #   这种禁用编辑链接的放法只是不让它在页面中显示，即把超链接去掉了，
     #   但是还是可以通过手动输入url的方式来进入编辑页面。
     #   不过可以配合设置fieldsets或者readonly_fieldss来达到目的
     #   注意：这里建议删除按钮要禁用掉，否则只有拥有view权限的人员依然可以进行删除动作，或者需要进行人员角色判断
     # """

    def has_add_permission(self, request):
        # 禁用添加按钮
        return True

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return True

@admin.register(Network)
class Network(admin.ModelAdmin):
    # 设置页面可以展示的字段
    list_display = ('version', 'router', 'case', 'status', 'msg', 'elapsed', 'start_time', 'end_time')
    # 默认不配置的话，第一个字段会存在链接到记录编辑页面
    list_display_links = None
    # list_display_links = ('uid',)
    # 设置过滤选项
    list_filter = ('version', 'router', 'case', 'status')
    # 每页显示条目数 缺省值100
    list_per_page = 15
    # show all页面上的model数目，缺省200
    list_max_show_all = 200
    # 设置可编辑字段 如果设置了可以编辑字段，页面会自动增加保存按钮
    # list_editable = ('IN_PARA_COMMENT',)
    # 按日期月份筛选 该属性一般不用
    # date_hierarchy = 'CREATED_TIME'
    # 按连接时间降序排序
    ordering = ('-end_time',)
    # 搜索条件设置
    # search_fields = ('msg',)

    # 增加自定义按钮
    actions = ['visualization']

    def visualization(self, request, queryset):
        print(queryset[0])
        return redirect("/visualize/" + str(queryset[0]) + "/")

    # 显示的文本，与django admin一致
    visualization.short_description = '可视化'
    # icon，参考element-ui icon与https://fontawesome.com
    # visualization.icon = 'fas fa-audio-description'
    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    visualization.type = 'danger'
    # 给按钮追加自定义的颜色
    # custom_button.style = 'color:black;'
    # visualization.action_type = 0
    # visualization.action_url = 'show/'

    # 表头字段显示中文名称，这里需要修改models文件，在定义字段的时候增加别名
    # eg1：JOB_NAME = models.CharField('任务名称',max_length=128)
    # eg2: name = models.CharField(max_length=30,verbose_name=u"姓名")

    # 字段关联展示
    ## 场景1、关联其他表的数据展示，此处外键展示不做演示，生产环境尽量减少外键使用

    ## 场景2、枚举信息转义展示
    ###  此处需要在model定义页面通过枚举值转义配置对应展示中文信息,参考model模块代码设置

     # """
     #   这种禁用编辑链接的放法只是不让它在页面中显示，即把超链接去掉了，
     #   但是还是可以通过手动输入url的方式来进入编辑页面。
     #   不过可以配合设置fieldsets或者readonly_fieldss来达到目的
     #   注意：这里建议删除按钮要禁用掉，否则只有拥有view权限的人员依然可以进行删除动作，或者需要进行人员角色判断
     # """

    def has_add_permission(self, request):
        # 禁用添加按钮
        return True

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return True
'''


@admin.register(TT)
class Tt(admin.ModelAdmin):
    # 设置页面可以展示的字段
    list_display = (
        'version', 'router', 'case', 'category', 'status', 'msg', 'standard', 'real', 'elapsed', 'start_time',
        'end_time', 'environment', 'rssi', 'channel', 'bandwidth')
    # 默认不配置的话，第一个字段会存在链接到记录编辑页面
    # list_display_links = None
    # list_display_links = ('uid',)
    # 设置过滤选项
    list_filter = ('version', 'router', 'category', 'status')
    # 每页显示条目数 缺省值100
    list_per_page = 15
    # show all页面上的model数目，缺省200
    list_max_show_all = 200
    # 设置可编辑字段 如果设置了可以编辑字段，页面会自动增加保存按钮
    # list_editable = ('IN_PARA_COMMENT',)
    # 按日期月份筛选 该属性一般不用
    # date_hierarchy = 'CREATED_TIME'
    # 按连接时间降序排序
    ordering = ('-end_time',)
    # 搜索条件设置
    # search_fields = ('msg',)

    # 增加自定义按钮
    actions = ['visualization']

    def visualization(self, request, queryset):
        print(queryset[0])
        return redirect("/visualize/" + str(queryset[0]) + "/")

    # 显示的文本，与django admin一致
    visualization.short_description = '可视化'
    # icon，参考element-ui icon与https://fontawesome.com
    # visualization.icon = 'fas fa-audio-description'
    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    visualization.type = 'danger'

    # 给按钮追加自定义的颜色
    # custom_button.style = 'color:black;'
    # visualization.action_type = 0
    # visualization.action_url = 'show/'

    # 表头字段显示中文名称，这里需要修改models文件，在定义字段的时候增加别名
    # eg1：JOB_NAME = models.CharField('任务名称',max_length=128)
    # eg2: name = models.CharField(max_length=30,verbose_name=u"姓名")

    # 字段关联展示
    ## 场景1、关联其他表的数据展示，此处外键展示不做演示，生产环境尽量减少外键使用

    ## 场景2、枚举信息转义展示
    ###  此处需要在model定义页面通过枚举值转义配置对应展示中文信息,参考model模块代码设置

    # """
    #   这种禁用编辑链接的放法只是不让它在页面中显示，即把超链接去掉了，
    #   但是还是可以通过手动输入url的方式来进入编辑页面。
    #   不过可以配合设置fieldsets或者readonly_fieldss来达到目的
    #   注意：这里建议删除按钮要禁用掉，否则只有拥有view权限的人员依然可以进行删除动作，或者需要进行人员角色判断
    # """

    def has_add_permission(self, request):
        # 禁用添加按钮
        return True

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return True


@admin.register(IOT)
class Iot(admin.ModelAdmin):
    # 设置页面可以展示的字段
    list_display = (
        'version', 'router', 'case', 'category', 'status', 'msg', 'standard', 'real', 'elapsed', 'start_time',
        'end_time', 'environment', 'rssi', 'channel', 'bandwidth')
    # 默认不配置的话，第一个字段会存在链接到记录编辑页面
    # list_display_links = None
    # list_display_links = ('uid',)
    # 设置过滤选项
    list_filter = ('version', 'router', 'category', 'status')
    # 每页显示条目数 缺省值100
    list_per_page = 15
    # show all页面上的model数目，缺省200
    list_max_show_all = 200
    # 设置可编辑字段 如果设置了可以编辑字段，页面会自动增加保存按钮
    # list_editable = ('IN_PARA_COMMENT',)
    # 按日期月份筛选 该属性一般不用
    # date_hierarchy = 'CREATED_TIME'
    # 按连接时间降序排序
    ordering = ('-end_time',)
    # 搜索条件设置
    # search_fields = ('msg',)

    # 增加自定义按钮
    actions = ['visualization']

    def visualization(self, request, queryset):
        print(queryset[0])
        return redirect("/visualize/" + str(queryset[0]) + "/")

    # 显示的文本，与django admin一致
    visualization.short_description = '可视化'
    # icon，参考element-ui icon与https://fontawesome.com
    # visualization.icon = 'fas fa-audio-description'
    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    visualization.type = 'danger'

    # 给按钮追加自定义的颜色
    # custom_button.style = 'color:black;'
    # visualization.action_type = 0
    # visualization.action_url = 'show/'

    # 表头字段显示中文名称，这里需要修改models文件，在定义字段的时候增加别名
    # eg1：JOB_NAME = models.CharField('任务名称',max_length=128)
    # eg2: name = models.CharField(max_length=30,verbose_name=u"姓名")

    # 字段关联展示
    ## 场景1、关联其他表的数据展示，此处外键展示不做演示，生产环境尽量减少外键使用

    ## 场景2、枚举信息转义展示
    ###  此处需要在model定义页面通过枚举值转义配置对应展示中文信息,参考model模块代码设置

    # """
    #   这种禁用编辑链接的放法只是不让它在页面中显示，即把超链接去掉了，
    #   但是还是可以通过手动输入url的方式来进入编辑页面。
    #   不过可以配合设置fieldsets或者readonly_fieldss来达到目的
    #   注意：这里建议删除按钮要禁用掉，否则只有拥有view权限的人员依然可以进行删除动作，或者需要进行人员角色判断
    # """

    def has_add_permission(self, request):
        # 禁用添加按钮
        return True

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return True
