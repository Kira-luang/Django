# 1.if使用
'''
{% if %}
{% elif %}
{% else %}
{% end if %}
'''

# 2.点应用
'''
类似于python语法
list1=[1, 3]
{{ list1[1] }}
dict1 = {'kira': 12}
{{ dict1.kira }}
student = Student()
student.xx -> 实例属性
'''

# 3.for循环(进阶版)
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

# 4.隐藏注释
'''
{# 内容 #} -> 单行注释(快捷键control+/)
多行注释:
{% commend %}
内容
{% endcommend %}
'''

# 5.乘除算法(比较少用)
'''
{% widthratio xx 1 3 %} -> 1是分母,3是分子
'''
