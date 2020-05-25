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


class Template:
    '''模板语言'''
    pass


# 1.占位(单个字符)
'''
在调用函数返回值的HttpResponse中，增加参数。例如:name='kira'
模板中:{{ name }}
'''

# 2.for循环
'''
在调用函数返回值的HttpResponse中，增加参数。例如:name=[1, 3, 2]/{'a'=1, 'b'=2}
模板中:{% for x in name %}
        {{ x }}
'''

# 3.render原理简单了解
'''
render:先加载(读取)模板html->对模板语言(python编译)->最后HttpResponse返回
'''

