# 1.URL关键词参数匹配
'''
URL设置形式:re_path('p29/(?P<year>\w+)/', views.p29)
year将会作为参数,传到p29的year上
'''

# 2.URL反向解析
'''
优化路劲:给路劲做代号,不用写成绝对路劲
作用:当路劲需要修改名字时,可以不用修改全部相关的模板url,直接修改url原名字即可

re_path('^student/', include(('App2.url')) 一级目录更名参考:详情看源码
re_path('^student/', include(('App2.url', 'App2'), namespace='student'))

被调用路劲re_path('checkstudent/', views.check_student) 二级目录更名参考
re_path('checkstudent/', views.check_student, name='check'),

URL反向解析格式:{% url 'student:check' %}
<p><a href="{% url 'student:check' %}">查看全部学生</a></p>
Tip:代号只是在引用(相当于变量),经过内部解析最后展现的页面是一种绝对路劲
也就是说,即使用了代号,原来的绝对路劲依然是可以用的！
'''

# 3.URL反向解析(位置带参)
'''
前提概述:URL的映射本质是"访问某个URL便会执行某个函数，返回的是数据+模板"
<p><a href="{% url 'student:p28' 'kira' %}">带参函数的应用</a></p> -> kira是参数,可写多个
'''

# 4.URL反向解析(key-value)
'''
<p><a href="{% url 'student:p29' mouth=5 year=2020 %}">带参函数的应用</a></p>
'''
