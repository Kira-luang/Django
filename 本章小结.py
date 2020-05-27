# 1.sql的limit和offset的映射
'''
Queryset[1: 5]-> 获取从第1到第5索引的数据
limit=4 -> 获取四条数据
offset=1 -> 也就是第二条数据
默认offset是0
'''

# 2.render的context参数作用
'''
以后都这样写，避免遗忘
自动创建一个字典，context={'a': 1}
render(request, context=context)
'''
