# 1.与mysql数据库进行连接
'''
配置文件(settings.py)的DATABASES添加:
'ENGINE': 'django.dbbackends.mysql',
'NAME': 'test',
'USER': 'kira',
'PASSWORD': 'abcd12345',
'HOST': '127.0.0.1',
'PORT': '3306'
Django自带的sqlite3注释掉
'''

# 2.pymysql进行伪装
'''
在settings.py所在目录的init.py上导入:
import pymysql

pymysql.install_as_MySQLdb()
'''

# 3.映射到mysql
'''
跟sqlite3一样的操作
python manage.py migrate
'''
