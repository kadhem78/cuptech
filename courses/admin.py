from django.contrib import admin

# Register your models here.
from .models import Subject , Course , Enrolments , Module
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    #list_display = ('title', 'instructor')
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    #list_display = ('title', 'instructor')
    #list_filter = ('Subject' , 'instructor' , 'created' , 'active')
    pass

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    #list_display = ('title', 'instructor')
    pass

@admin.register(Enrolments)
class EnrolmentsAdmin(admin.ModelAdmin):
    list_filter = ('course',)
