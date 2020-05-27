from django.shortcuts import render, HttpResponse


# Create your views here.
from App2.models import Student, Class


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
