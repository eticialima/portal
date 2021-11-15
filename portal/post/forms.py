from django import forms
from post.models import Post, Tag, Category
 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'desc', 'image','download_file','download_link','created_date','published_date','category','tags')

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'