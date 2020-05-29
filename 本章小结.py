# 实操前端输入数据到后台
'''
form + tab
input + tab

基本格式出来了,在form里加上method
在input里加上name和placeholder就完成了
'''

# cookie(默认不支持中文)
'''
render和HttpResponse都有set_cookie
rende.set_cookie('name', entity.name)
set_cookie参数
max_age->设置最大时长(即使关闭浏览器也还存在cookie)
expire->直接设置日期
获取cookie: request.COOKIE.get() -> get设置的cookie即可

加密cookie
rende.set_signed_cookie('name', entity.name, 'test')
解密获取cookie:
cookie = request.get_signed_cookie('name', salt='test')
'''

# django.middleware.csrf.CsrfViewMiddleware
'''
csrf:跨站请求伪造,由于与前端输入数据冲突,暂时性注释
在settings文件的MIDDLEWARE里
'''

# 尝试实现cookie存储中文(利用base64编解码即可)
import base64

str1 = 'sda12英语ffs47是'
base = base64.b64encode(str1.encode())
print(base64.b64encode(str1.encode()))
print(base64.b64decode(base).decode())
