from django.urls import path, re_path

from App2 import views

urlpatterns = [
    re_path('addstudent/', views.addstudent),
    re_path('kira/', views.response),
    re_path('updatestudent/', views.update_student),
    re_path('checkstudent/', views.check_student),
    re_path('delestudent/', views.dele_student),
    re_path('addclass/', views.add_class),
    re_path('companycp/', views.compare),
    re_path('select/', views.select),
]
