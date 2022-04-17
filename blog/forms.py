from .models import Post
from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class PostForm(ModelForm):
    content = forms.CharField(widget= CKEditorUploadingWidget())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categorie'].widget.attrs.update({'class': 'form-control'} )
        self.fields['header_img'].widget.attrs.update({'class': 'custom-file-input'})
        self.fields['title'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'title'})
        self.fields['content'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'post content'})
    class Meta:
        model = Post
        fields = ['categorie' , 'header_img' , 'title' , 'content']
