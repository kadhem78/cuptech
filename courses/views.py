from django.shortcuts import render , redirect
from .models import Subject , Course , Module , Enrolments
from .forms import CourseForm , ModuleForm
from django.urls import reverse
# Create your views here.


def manage_courses(request):
    courses = Course.objects.filter(instructor = request.user)
    context = {
    'courses' : courses
    }
    return render(request , 'managecourses/manage_courses.html' , context)


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST , request.FILES)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.instructor = request.user
            new_form.save()
            return redirect('manage_courses')
    else:
        form = CourseForm()

    context = {
    'form' : form
    }
    return render(request , 'managecourses/createcourse.html' , context)


def update_course(request , slug):
    course = Course.objects.get(slug = slug)
    print('done')
    if request.method == 'POST':
        form = CourseForm(request.POST , request.FILES , instance = course )
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.instructor = request.user
            new_form.save()

            return redirect(reverse('manage_courses'))
    else:
        form = CourseForm(instance = course)

    context = {
    'form' : form
    }
    return render(request , 'managecourses/updatecourse.html' , context)

def delete_course(request , slug):
    course = Course.objects.get(slug = slug).delete()
    return redirect(reverse('manage_courses'))


def courses_list(request):
    courses = Course.objects.filter(active = True)
    context = {
    'courses' : courses
    }
    return render(request , 'courses.html' , context)

def course_details(request , slug):
    course = Course.objects.get(slug = slug)
    context = {
    'course' : course
    }
    return render(request , 'course_details.html' , context)


def enrolement(request , slug):
    course = Course.objects.get(slug=slug)
    enrolement = Enrolments.objects.get(student = request.user , course = course)
    if enrolement :
        return redirect(reverse('course_details', args = [slug]))
    else:
        Enrolments.objects.create(course = course , student = request.user)
        return redirect(reverse('course_details', args = [slug]))

def module_list(request,slug):
    modules = Module.objects.all()
    course = Course.objects.get(slug = slug)
    context = {
    'modules' : modules ,
    'course' : course
    }
    return render(request , 'modulelist.html' , context)

def add_module(request , slug):
    course = Course.objects.get(slug = slug)
    if request.method == 'POST':
        form = ModuleForm(request.POST , request.FILES)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.course = course
            new_form.save()
            return redirect(reverse('module_list' , args = [course.slug]))
    else :
        form = ModuleForm()
    context = {
    'form' : form
    }
    return render(request , 'managecourses/addmodule.html' , context)

def update_module(request , pk):
    pass

def delete_module(request , pk):
    pass

