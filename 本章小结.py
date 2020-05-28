# 1.Django联合主键
'''
在基类中增加,unique_together
class Meta:
    unique_together = ('name', 'item')
把name和item合并作为唯一键,并且两者不能为null->等价于联合主键
'''
