# 1.get用法展开
'''
Student.objects.get(name='kira')
get不要传单参,要传以上方式
get不一定要传入主键,条件限制到只能一个数据符合即可。
'''

# 2.ForeignKey创建
'''
models.ForeignKey('类名', on_delete=models.CASCADE)
'''

# 3.正向查询
'''
student = Student.objects.get()->拿到实例
student.id.item
(外键字段)  所查询字段
'''

# 4.反向查询
'''
a = Class.objects.get()
a.student_set.all()
'''
