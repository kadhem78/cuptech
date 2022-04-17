from .models import Course , Module
from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class CourseForm(ModelForm):
    description = forms.CharField(widget= CKEditorUploadingWidget())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs.update({'class': 'form-control'} )
        self.fields['course_img'].widget.attrs.update({'class': 'custom-file-input'})
        self.fields['title'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'title'})
        self.fields['description'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'course description'})
    class Meta:
        model = Course
        fields = ['subject' , 'course_img' , 'title' , 'description']

class ModuleForm(ModelForm):
    content = forms.CharField(widget= CKEditorUploadingWidget())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'title'})
        self.fields['content'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'course description'})
    class Meta:
        model = Module
        fields = ['title' , 'content']
