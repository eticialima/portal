import django_filters
from post.models import Post, Category, Tag
from django import forms

class PostFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name='author__user_name', lookup_expr='icontains') 
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple) 
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Post
        fields = ['author', 'title', 'category', 'tags']
        #fields = {'title':['exact', 'contains']}
