from django import forms
from django.forms.widgets import NumberInput
from post.models import Post, Category   
from django.conf import settings 

class DateInput(forms.DateInput):
    input_type = 'date' 
    
class PostForm(forms.ModelForm): 
    published_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)
     
    class Meta:
        model = Post
        fields = ('author', 'title', 'desc', 'image','download_file','download_link','created_date','published_date','is_activate', 'category','tags')
 
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__' 