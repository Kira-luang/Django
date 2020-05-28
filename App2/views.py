from django.db.models import Max, F, Q
from django.shortcuts import render, HttpResponse


# Create your views here.
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
    return render(request, 'p21.html', context=context)
