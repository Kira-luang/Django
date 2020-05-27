# 1.理论删除的意思
'''
数据库一般只存在理论删除，不存在物理删除
设置一个BooleanField字段,理论删除就是把该字段值改为False
'''

# 2.为什么对数据进行操作时都要经过objects？
'''
每一个ORM模型的class,都有一个隐藏属性objects=models.Manager()->objects是models.Manager的一个实例
而这个objects就是对类属性进行管理的属性
'''

# 3.预筛选(预设查询条件)
'''
已知objects的来历,那么只需要用任意一个属性test=models.Manager()
这个objects隐藏属性就不会再被添加,所以只能通过class.test.属性来访问属性

定义一个Manager类
class Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(girl__gt=10)
在class Company显式添加属性管理
objects = Manager()

实例解说:
compar = Company.objects.filter(boy__lt=F('girl') - 5)
Company.objects会先筛选出girl__gt=10的Queryset
然后再对这个Queryset再进行filter
'''
