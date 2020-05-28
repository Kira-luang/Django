# 模板的继承(重点)
'''
在第一个模板中作用:挖坑,规划布局
{% block xxx %}
{% endblock %}
在第二个继承模板中作用:填坑
在第三个继承模板中作用:填坑+默认覆盖(可以选择super增量式操作)

{{ block.super }}

继承:
{% extends base.html %}
{% endextends %}

调用其他html
{% include head.html %} -> 把head.html的内容嵌入当前html页面

Tip:能用block+extends就不要用include,include影响效率
'''
