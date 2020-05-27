# 1.聚合函数使用
'''
Avg,Sum,Count,Max,Min
Student.objects().aggregate(AVG()) -> 返回类型字典{字段:值}
Tip:聚合函数都需要导入
'''

# 2.同一个记录中两个字段之间进行比较
'''
Company.objects.filter(boy__lt=F('girl')-5)
需要导入F才能完成
'''

# 3.and,or,not
'''
and: &
or: |
not: ~
应用:Company.objects.filter(~(Q(boy__gt=60) | Q(girl__gt=70)))
需要导入Q才能完成
'''
