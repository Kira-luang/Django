# 添加CSS或者JS文件时,需要在settings里添加
'''
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), -> static是文件名
]

'''

# 绝对路劲改相对路劲(静态资源)
'''
{% load static %} -> 加载初始目录
href={% "static" 'css/xxx.css' %} -> 相对于static目录的路劲
只能在debug里处理
'''