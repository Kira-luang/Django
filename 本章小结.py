# 过滤器操作以及格式
'''
格式: {{var | 过滤器}}
{% x | divisible by 2 %}->"|"表示把x代入divisible by 2中
divisible by 2->能够被2整除,配合if使用(过滤器)

加法:{{var |add:6}} -> 加6
减法:{{var |add:-6}} -> 减6
大写:{{var |upper}} -> 了解即可
小写:{{var |lower}} -> 了解即可
默认值:{{var |default value}} -> 了解即可
函数传参:{{var |join"参数"}} -> 了解即可
日期:{{var |data:'y-m-d'}} -> 了解即可
'''
