# HttpResponse的子类:HttpResponseRedirect(302)
'''
HttpResponseRedirect()的应用 -> redirect()是其短写
可以实现服务器内部重定向
def p30(request):
    return HttpResponse('你被阻塞了')


def p30_main(request):
    if random.randint(1, 10) > 5:
        return HttpResponseRedirect('/student/p30/GG') -> 硬编码
    return HttpResponse('成功返回')

可转换为:
url = reverse('student:GG') -> 跟模板语法一样
HttpResponseRedirect(url)
'''

# json知识
'''
json的两种形式:
JsonObject:
最常见,key:value"{}"形式
JsonArray
以列表"[]"形式,可包含JsonObject

两者可嵌套
'''

# HttpResponse的子类:JsonResponse
'''
以json的形式返回 -> 用于前后端分离,Ajax

return JsonResponse(data) data->是字典形式
'''

'''更多子类可以直接看源码,专门针对状态码,原理是修改HttpResponse的status_code属性,返回内容依然自定义'''
