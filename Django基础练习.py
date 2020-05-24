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
