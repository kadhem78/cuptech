from django.contrib import admin
from django.urls import path
from courses import views as courses_views

urlpatterns = [
    path('manage_courses/' , courses_views.manage_courses , name='manage_courses'),
    path('create/' , courses_views.create_course , name='create_course'),
    path('update/<slug:slug>' , courses_views.update_course , name='update_course'),
    path('delete/<slug:slug>' , courses_views.delete_course , name='delete_course'),
    path('<slug:slug>/' , courses_views.course_details , name='course_details'),
    path('<slug:slug>/enrole' , courses_views.enrolement , name='enrolement'),
    path('<slug:slug>/add_module' , courses_views.add_module , name='add_module'),
    path('<slug:slug>/modules' , courses_views.module_list , name='module_list'),
    path('' , courses_views.courses_list , name='courses_list'),
]
