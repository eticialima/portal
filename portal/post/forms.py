from django import forms
from post.models import Post
 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'desc', 'image','download_file','download_link','created_date','published_date')
