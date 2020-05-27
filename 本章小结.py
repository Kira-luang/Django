# 懒查询
'''
all,filter,exclude
类似于生成器，只有执行迭代或者获取数据才会真正地去数据库查询。
'''

# Django时间坑
'''
Django默认使用的是自己的time_zone,会出现查询错误
打开settings文件，把USE_TZ=True改成False即可
'''

# 13.查询条件
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
