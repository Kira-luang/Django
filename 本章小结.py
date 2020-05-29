# 404,500,502页面设置
'''
在templates模板里创建html即可
'''

# 前端输入post上传信息代码
'''
<form action={% url "路劲" %} method="post">
    <span>username:</span> <input type="text" name="username" placeholder="please input your name">
    <button>submit</button>
</form>

action就是操作,method选择post,给用户提交
input参数,type就是类型,name就是给传过来参数取名,placeholder是提示
'''
