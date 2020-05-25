# 1.ORM查
'''
1.查全部数据
Student.objects.all()
2.查/获取某个数据
Student.objects.get()
'''

# 2.ORM删,改
'''
都要先拿到对象
obj = Student.objects.get(name='tom')
然后才能进行删改
obj.delete()/obj.name = 'Tom'
对于对数据进行处理的操作都要保存才能同步到数据库
obj.save()
'''

# 3.模板语言:for
'''
在调用函数返回值的HttpResponse中，增加参数。例如:name=[1, 3, 2]/{'a'=1, 'b'=2}
模板中:{% for x in name %}
        {{ x }}

这里是传入从数据库匹配到的数据,格式为:[数据对象1(多个属性值组合的字典), 数据对象2(多个属性值组合的字典)]
所以这里遍历之后,提取拿name属性
'''
