from django.urls import path, re_path

from App2 import views

urlpatterns = [
    re_path('addstudent/', views.addstudent),
    re_path('^kira/$', views.response),
    re_path('updatestudent/', views.update_student),
    re_path('checkstudent/', views.check_student, name='check'),
    re_path('delestudent/', views.dele_student),
    re_path('addclass/', views.add_class),
    re_path('companycp/', views.compare),
    re_path('select/', views.select),
    re_path('p21/', views.p21),
    re_path('^p28/$', views.p28_main),
    re_path('^p28/(\w+)/', views.p28, name='p28'),
    re_path('p29/(?P<year>\w+)/(?P<mouth>\w+)/', views.p29, name='p29'),
    re_path('p34/main', views.p34_main),
    re_path('p34/GG', views.p34, name='GG'),
    re_path('p34/json', views.p34_json, name='json'),
    re_path('p35/register', views.p35_register, name='register'),
    re_path('p35/work', views.p35_work, name='work'),
    re_path('p36/logout', views.p36_logout, name='logout'),
]
