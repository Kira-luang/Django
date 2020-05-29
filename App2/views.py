import random

from django.db.models import Max, F, Q
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect


# Create your views here.
from django.urls import reverse

from App2.models import Student, Class, Company, A


def response(request):
    return HttpResponse('<h1>Hello Dear</h1>')


def addstudent(request):
    student = Student()
    student.name = input('your name')
    student.age = 10
    student.save()
    return HttpResponse('成功调用')


def update_student(request):
    obj = Student.objects.get(name='Kira')
    obj.name = 'Tom'
    obj.save()
    return HttpResponse('成功修改')


def check_student(request):
    obj = Student.objects.filter(age__lt=24).order_by('id')[1:3]
    all_student = Student.objects.all()
    oldstudent = Student.objects.aggregate(Max('age'))
    print(oldstudent)
    context = {'obj': obj, 'all': all_student}
    return render(request, 'checkstudent.html', context=context)


def dele_student(request):
    obj = Student.objects.get(name='tom')
    obj.delete()
    obj.save()
    return HttpResponse('删除成功')


def add_class(request):
    entity = Class.add_class()
    entity.save()
    return render(request, 'add_class.html', {'body': '成功添加'})


def compare(request):
    compar = Company.objects.filter(boy__lt=F('girl') - 5)
    for x in compar:
        print(x.company)
    return HttpResponse('测试成功')


def select(request):
    x = Company.manage.filter(~(Q(boy__gt=60) | Q(girl__gt=70)))
    for y in x:
        print(y.company)
    return HttpResponse('测试成功')


def p21(request):
    context = {'class': A}
    print(request.path)
    return render(request, 'p21.html', context=context)


def p28_main(request):
    entity = Student.objects.all()
    return render(request, 'p28.html', context=locals())


def p28(request, name):
    entity = Student.objects.get(name=name)
    return HttpResponse('Hello {} your item is {}'.format(name, entity.id.item))


def p29(request, year, mouth):
    context = {'year': year, 'mouth': mouth}
    return render(request, 'p29.html', context=context)


def p34(request):
    Reponse = HttpResponse('你被阻塞了')
    Reponse.status_code = 304
    return Reponse


def p34_main(request):
    if random.randint(1, 10) > 5:
        url = reverse('student:GG')
        return HttpResponseRedirect('/student/p30/GG')  # 这是302状态
    return HttpResponse('成功返回')


def p34_json(request):
    data = {
        'kira': 24,
        'zeno': 23,
    }
    return JsonResponse(data)
