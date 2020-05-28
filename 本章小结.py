# URL的组成
'''URL:https://www.bilibili.com/video/BV1rx411X717?p=28#footer'''
'''
协议: http/https/ftp
域名/IP+port: www.bilibili.com/127.0.0.1:8000
path: video
GET请求参数/QueryString(查询参数)：BV1rx411X717?p=28
描点:以#为分割
'''

# 实践通过输入路劲,查询到相关信息
'''
思路:创建一个主模板,作为一个目录；创建一个分模板,能够接受捕获URL的path进行处理

student和class
通过输入名字,查询到名字相对应的科目
熟练后尝试反向查询
'''
