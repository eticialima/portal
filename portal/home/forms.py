from django import forms
from post.models import Post, SocialComment


class SocialPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': '3',
            'placeholder': 'Say Something...'
            }),
        required=True) 
	
    class Meta:
        model=Post
        fields=['body']


class SocialCommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': '1',
            'placeholder': 'Comment Something...'
            }),
        required=True
        )

    class Meta:
        model=SocialComment
        fields=['comment']


class ShareForm(forms.Form):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': '3',
            'placeholder': 'Say Something...'
            }),
        )