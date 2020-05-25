# 1.创建与连接数据库
'''
远程连接数据库
右边的Database->'+'database resource->填配置信息
Django自带数据库
右键db.sqlite3->新建datasource->path为db.sqlite3->driver是SQLite
'''

# 2.ROM模型(创建表格)
'''
在models.py里建立类->python manage.py makemigrations->python manage.py migrate
'''

# 3.ORM数据模型:增
'''
student = Student()->创建实例
student.name = 'kira'
student.age = 10
student.save()->提交到数据库
'''

# 4.ORM数据模型:查
'''
Student.object.all()
'''
