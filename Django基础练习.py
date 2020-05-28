# 1.创建连接与回应(要正则表达式)
'''
urls.py -> urlpatterns里进行注册 -> re_path('^kira', views.response)
正则表达式需要导入re_path

App.views.py -> 新增回应函数 -> return HttpResponse('Hello Kira')
HttpResponse需要from django.shortcuts import render
'''

# 2.回应关联html
'''
创建templates -> index.html
render(request, 'index.html')
Tip:render需要from django.shortcuts import render

设置settings.py -> install_app新增App文件
'''

# 3.创建分支路由
'''
python manage.py runserver startapp App2
settings.py->在INSTALLED_APPS内加上App2
在App2创建url.py -> 复制urls的路由代码
在views添加回复函数
urls.py导入include,增加路劲 -> re_path('^student', include('App2.url'))
'''

# 4.文件使用介绍
'''
admin.py:后台管理模块
apps.py:管理站点模型的声明文件
models.py:对应数据库作映射(定义表对应的class)
views.py:给对应URL作处理
migrations:把对应数据库表的class暂时存储的地方(在sqlite做完测试,要换mysql时，可直接把class映射在mysql上)
tests.py:代码测试模块
settings.py:配置模块
'''


class Model:
    '''主要针对数据库，也就是Model模块'''


# 4.创建与连接数据库
'''
远程连接数据库
右边的Database->'+'database resource->填配置信息
Django自带数据库
右键db.sqlite3->新建datasource->path为db.sqlite3->driver是SQLite
'''

# 5.ROM模型(创建表格)
'''
在models.py里建立类->python manage.py makemigrations->python manage.py migrate
'''

# 6.ORM数据模型:增
'''
student = Student()->创建实例
student.name = 'kira'
student.age = 10
student.save()->提交到数据库
'''

# 7.ORM数据模型:查
'''
Student.object.all()
'''

# 8.Django外键
'''
当外键是一对一时，必须添加on_delete，外键参考
Aid = models.ForeignKey('一个外键类(外键表)', on_delete=models.CASCADE)
外键(Aid)传入值的时候需要传入外键所在表的实例
'''

# 9.外键正反向查询
'''
假设Student外键是Class
obj = Student.objects.get(name='kira')->都要先获得实例(字段)
正向查询:
obj.ForeignKey(字段).(class对应的某个字段)
反向查询:
obj.student_set.all()
'''

# 10.Django的field大全
'''
TextField:大字符串(长度大于4000)
DecimalField:高精度数字(金融应用)
BooleanField:True/False
NullBooleanField:True/False/Null(可用于性别)
DatatimeField:时间
FileField/ImageField:把文件/图片进行编译存储到数据库(不推荐使用)
外键Field定义:
ForeignKey:一对多
ManyToManyField:多对多
OneToOneField:一对一
'''

# 11.类属性大全
'''
null:空值 -> 数据库展现的是NULL
blank:空值(类似空字符串的形式) -> 数据库展现的是空
db_column:字段名
db_index:创建索引
default:默认值 (这个默认值并不会转换成sql,会在你添加实例时默认给你加上)
primary_key:主键
unique:唯一键
'''

# 12.基类Meta的作用:更改表名 & 排序 & 实现联合键
'''
在ORM的类对象里增加基类
class Meta:
    db_table = 'student' -> 更改表名
    ordering = [] -> 排序
    unique_together = () -> 实现联合键
student为自定义类名
'''

# 13.筛选
'''
filter:符合条件的数据；exclude:不符合条件的数据 -> 可连用
student.objects.filter(条件)
student.objects.exclude(条件)
'''

# 14.查询条件
'''
__gt(大于),__lt(小于)
__gte(大于等于),__lte(小于等于)
__in(在某个集合之中)
__contains(包含，类似like)
__startswith(开头)，__endswith(结尾)
忽略大小写:
__icontains
其他命令也是这含义
'''

# 15.预筛选(预设查询条件)
'''
已知objects的来历,那么只需要用任意一个属性test=models.Manager()
这个objects隐藏属性就不会再被添加,所以只能通过class.test.属性来访问属性

定义一个Manager类
class Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(girl__gt=10)
在class Company显式添加属性管理
objects = Manager()

实例解说:
compar = Company.objects.filter(boy__lt=F('girl') - 5)
Company.objects会先筛选出girl__gt=10的Queryset
然后再对这个Queryset再进行filter
'''

'''多个数据组合成的并不是列表,而是一个Queryset'''


class Template:
    '''模板语言'''
    pass


# 1.占位(单个字符)
'''
在调用函数返回值的HttpResponse中，增加参数。例如:name='kira'
模板中:{{ name }}
'''

# 2.for循环(简答应用)
'''
在调用函数返回值的HttpResponse中，增加参数。例如:name=[1, 3, 2]/{'a'=1, 'b'=2}
模板中:{% for x in name %}
        {{ x }}
       {% endfor %}
'''

# 3.render原理简单了解
'''
render:先加载(读取)模板html->对模板语言(python编译)->最后HttpResponse返回
'''

# 4.if使用
'''
{% if %}
{% elif %}
{% else %}
{% end if %}
'''

# 5.点应用
'''
类似于python语法
list1=[1, 3]
{{ list1[1] }}
dict1 = {'kira': 12}
{{ dict1.kira }}
student = Student()
student.xx -> 实例属性
'''

# 6.for循环(进阶版)
'''
list1 = []
{% for x in list1 %}
    {{ forloop counter }}{{ x }} -> 循环次数计数
    {% empty %} -> 当列表为空时便会执行
    空列表
{% endfor %}

forloop.counter表示循环计数
forloop.counter0从0开始计数
forloop.revcounter倒数计数,直到1为止
forloop.revcounter0倒数计数,直到0为止
forloop.first如果当前循环是第一个就是True
forloop.last如果当前循环是最后一个就是True
'''

# 7.隐藏注释
'''
{# 内容 #} -> 单行注释(快捷键control+/)
多行注释:
{% commend %}
内容
{% endcommend %}
'''

# 8.乘除算法(比较少用)
'''
{% widthratio xx 1 3 %} -> 1是分母,3是分子
'''

# Django流程:
'''
1.创建项目: django-admin startproject mysite
2.创建应用程序:python manage.py startapp App
3.创建路由与对应的回应->修改urls和views
4.建立与数据库的连接->修改settings的database
5.建立模型(ORM)
6.对数据库进行关联->迁移(python manage.py makemigrations/python manage.py migrate)
'''

# 完成项目时配置文件必改项
'''
DEBUG=False -> 关闭调试
ALLOWED_HOSTS = ['*'] -> 接受访问
LANGUAGE_CODE = 'zh-hans' -> 修改为汉字
TIME_ZONE = 'Asia/Shanghai' -> 修改成上海时间
USE_TZ = False -> 时间机制不用Django的Time_Zone
DATABASES = 你的Mysql配置(具体参考空间)
pymysql的伪装->在当前文件夹的init上伪装
'''
